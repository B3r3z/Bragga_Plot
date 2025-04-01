# Bragga_Plot# Siatka Bragga – Analiza charakterystyki odbiciowej

Ten projekt zawiera kod w Pythonie do analizy charakterystyki odbiciowej siatki Bragga w światłowodach. Kod został zaprojektowany tak, aby:

- Automatycznie obliczać grubość warstwy wysokiego współczynnika załamania \( a_H \) zgodnie z równaniem ćwierćfalowym:
  
  \[
  n_L \, a_L = n_H \, a_H \quad \Longrightarrow \quad a_H = \frac{n_L \, a_L}{n_H}
  \]
  
- Wyliczać charakterystykę odbiciową dla zadanych parametrów struktury.
- Obliczać szerokość pasma 3 dB (zarówno w dziedzinie długości fali, jak i częstotliwości).
- Rysować wykres charakterystyki odbiciowej z zaznaczonym poziomem 3 dB oraz granicami pasma.

## Wymagania

- Python 3.x
- Biblioteki: `numpy`, `matplotlib`

Możesz zainstalować wymagane pakiety za pomocą pip:

```bash
pip install numpy matplotlib
