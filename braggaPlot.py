import numpy as np
import matplotlib.pyplot as plt

# --- Parametry siatki Bragga ---
N = 8           # liczba okresów
n_L = 1.44      # współczynnik załamania warstwy L (zadany na sztywno)
n_H = 2.22      # współczynnik załamania warstwy H
a_L = 275       # grubość warstwy L [nm]

# --- Warunek ćwierćfalowy: n_L * a_L = n_H * a_H ---
# => a_H = (n_L * a_L) / n_H
a_H = (n_L * a_L) / n_H

# --- Pozostałe parametry ---
c_light = 3e8   # prędkość światła [m/s]
Lambda = a_L + a_H  # okres struktury [nm]

# --- Zakres długości fali ---
lambda_nm = np.arange(1000, 2201, 10)  # długości fali [nm]
lambda_m = lambda_nm * 1e-9            # konwersja do metrów

# --- Obliczenia ---
k_L = 2 * np.pi * n_L / lambda_nm
k_H = 2 * np.pi * n_H / lambda_nm

a = np.exp(1j * a_H * k_H) * (
    np.cos(k_L * a_L) 
    + (1j / 2) * (k_H / k_L + k_L / k_H) * np.sin(k_L * a_L)
)
d = np.exp(-1j * a_H * k_H) * (
    np.cos(k_L * a_L) 
    - (1j / 2) * (k_H / k_L + k_L / k_H) * np.sin(k_L * a_L)
)
b = np.exp(-1j * a_H * k_H) * (
    (1j / 2) * (k_L / k_H - k_H / k_L) * np.sin(k_L * a_L)
)
c = np.exp(1j * a_H * k_H) * (
    (1j / 2) * (k_H / k_L - k_L / k_H) * np.sin(k_L * a_L)
)

K = (1 / Lambda) * np.arccos((a + d) / 2)
tt = (np.sin(K * Lambda) / np.sin(N * K * Lambda)) ** 2
denom = np.abs(c) ** 2 + tt
R = np.abs(c) ** 2 / denom

# --- Obliczenia pasma 3 dB ---
R_max = np.max(R)
R_3db = R_max / 2

indices_above = np.where(R >= R_3db)[0]
lambda_3db_min = lambda_nm[indices_above[0]]
lambda_3db_max = lambda_nm[indices_above[-1]]
delta_lambda_3db_nm = lambda_3db_max - lambda_3db_min

# --- Obliczenie delta f (dokładnie) ---
lambda_center_nm = (lambda_3db_min + lambda_3db_max) / 2
lambda_center_m = lambda_center_nm * 1e-9
delta_f_precise_Hz = (c_light / lambda_center_m**2) * (delta_lambda_3db_nm * 1e-9)
delta_f_precise_GHz = delta_f_precise_Hz / 1e9

# --- Wykres ---
plt.figure(figsize=(10, 6))
plt.plot(lambda_nm, R, color='orange', linewidth=2, label='Odbiciowość')
plt.axhline(y=R_3db, color='red', linestyle='--', label='Poziom 3 dB')
plt.axvline(x=lambda_3db_min, color='green', linestyle='--', label='Granice pasma 3 dB')
plt.axvline(x=lambda_3db_max, color='green', linestyle='--')
plt.title('Charakterystyka odbiciowa siatki Bragga (ćwierćfalowa)', fontsize=16)
plt.xlabel('Długość fali (nm)', fontsize=14)
plt.ylabel('Odbiciowość', fontsize=14)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

# --- Wyniki ---
print(f"a_H (z warunku ćwierćfalowego) = {a_H:.2f} nm")
print(f"∆λ_3dB = {delta_lambda_3db_nm:.2f} nm")
print(f"∆f_3dB = {delta_f_precise_GHz:.2f} GHz")
