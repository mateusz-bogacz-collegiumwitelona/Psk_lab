import numpy as np
import matplotlib.pyplot as plt

def lehman_lcg(n_samples, L=16, a=5, seed=12345):
    m = 2**L
    x = seed 
    results_r = []
    
    for _ in range(n_samples):
        x = (a * x) % m
        results_r.append(x / m)
    return results_r

def f(x):
    return np.exp(-(x**2))

def solve_integral_mmc_with_plot(n_max):
    true_value = 0.7468241328
    print(f"Generowanie {n_max} liczb Lehmera...")
    x_samples = lehman_lcg(n_max)
    
    f_values = [f(x) for x in x_samples]
    
    print("Obliczanie zbieżności...")
    cumulative_sum = np.cumsum(f_values)
    num_samples_array = np.arange(1, n_max + 1)
    running_mean = cumulative_sum / num_samples_array
    
    plt.figure(figsize=(12, 6))
    plt.plot(num_samples_array, running_mean, label='Estymacja MMC (Lehmer)', color='blue', alpha=0.8)
    plt.axhline(y=true_value, color='red', linestyle='--', label=r'Prawdziwa wartość ($\approx 0.7468$)')
    
    plt.title(fr"Zbieżność metody Monte Carlo dla całki $\int_0^1 e^{{-x^2}} dx$" + f"\n(Generator Lehmera, N_max={n_max})")
    
    plt.xlabel(r"Liczba próbek ($N$)")
    plt.ylabel(r"Obliczona wartość całki")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    plt.figure(figsize=(10, 5))
    plt.hist(x_samples, bins=50, color='purple', edgecolor='black', alpha=0.7, density=True)
    
    plt.axhline(y=1, color='orange', linestyle='-', label='Idealny rozkład jednostajny U[0,1]', linewidth=2)
    
    plt.title(f"Histogram próbek z generatora Lehmera ($N={n_max}$)\n(Weryfikacja równomierności próbkowania)")
    plt.xlabel("Wartość próbki ($x_i$)")
    plt.ylabel("Gęstość")
    plt.grid(True, linestyle=':', alpha=0.6)
    plt.legend()
    
    # Wyświetlamy oba wykresy
    plt.tight_layout()
    plt.show()

    # Zwracamy końcowy wynik
    return running_mean[-1]

if __name__ == "__main__":
    N_MAX = 50000 
    
    print(f"--- Uruchamianie wizualizacji MMC ---")
    final_result = solve_integral_mmc_with_plot(N_MAX)
    
    print(f"\nKońcowy wynik całki (dla N={N_MAX}): {final_result:.6f}")
    print(f"Prawdziwa wartość: 0.746824")