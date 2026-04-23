import matplotlib.pyplot as plt

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  Błąd: podaj liczbę całkowitą!")

def read_L():
    while True:
        L = read_int("Podaj L (>= 4): ")
        if L >= 4:
            return L
        print("  Błąd: L musi być >= 4!")

def read_a():
    while True:
        a = read_int("Podaj a (nieparzyste, np. 3 lub 5): ")
        if a % 2 == 1 and a > 0:
            return a
        print("  Błąd: a musi być dodatnie i nieparzyste!")

def read_seed():
    while True:
        x = read_int("Podaj seed X0 (nieparzysty, > 0): ")
        if x % 2 == 1 and x > 0:
            return x
        print("  Błąd: X0 musi być dodatni i nieparzysty!")

L = read_L()
a = read_a()
x = read_seed()

def lehman_lcg(n_samples, L, a, x):
    m = 2**L
    results_r = []
    for _ in range(n_samples):
        x = (a * x) % m
        r = x / m
        results_r.append(r)
    print(f"Wygenerowano {len(results_r)} liczb. Pierwsze pięć: {results_r[:5]}")
    return results_r

def run_stats(data):
    n = len(data)
    if n < 2:
        print("Za mało danych.")
        return
    mean = sum(data) / n
    variance = sum((xi - mean)**2 for xi in data) / (n - 1)
    print("\n--- TESTY STATYSTYCZNE ---")
    print(f"Średnia:   {mean:.4f}    (oczekiwana: 0.5)")
    print(f"Wariancja: {variance:.4f} (oczekiwana: ~0.0833)")

def plot_2d(data):
    plt.figure(figsize=(8, 6))
    plt.scatter(data[:-1], data[1:], alpha=0.6, color='blue', s=15)
    plt.title("Test niezależności 2D ($r_n$ vs $r_{n+1}$)")
    plt.xlabel("$r_n$")
    plt.ylabel("$r_{n+1}$")
    plt.grid(True, linestyle='--')
    plt.show()

def plot_3d(data):
    fig = plt.figure(figsize=(9, 7))
    ax = fig.add_subplot(111, projection='3d')
    
    x_coords = data[:-2]
    y_coords = data[1:-1]
    z_coords = data[2:]
    
    ax.scatter(x_coords, y_coords, z_coords, alpha=0.6, color='red', s=15)
    ax.set_title("Test niezależności 3D ($r_n$, $r_{n+1}$, $r_{n+2}$)")
    ax.set_xlabel("$r_n$")
    ax.set_ylabel("$r_{n+1}$")
    ax.set_zlabel("$r_{n+2}$")
    plt.show()

samples = lehman_lcg(2000, L, a, x)
run_stats(samples)
plot_2d(samples)
plot_3d(samples)