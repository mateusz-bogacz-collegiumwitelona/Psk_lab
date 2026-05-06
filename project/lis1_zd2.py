import matplotlib.pyplot as plt

def von_neumann_generator(seed, n_samples):
    current = seed
    results = []
    
    for i in range(n_samples):
        square_str = str(current**2).zfill(8)
        
        middle_str = square_str[2:6]
        current = int(middle_str)
        
        results.append(current / 10000.0)
        if current == 0:
            current = 1234 + i 
            
    return results

def plot_2d_independence(data):
    x = data[:-1]
    y = data[1:]
    
    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, alpha=0.6, s=15, color='blue')
    plt.title("Test graficzny 2D: Von Neumann ($r_n$ vs $r_{n+1}$)")
    plt.xlabel("$r_n$")
    plt.ylabel("$r_{n+1}$")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.show()


def plot_3d_independence(data):
    # Tworzymy trójki (x, y, z)
    x = data[:-2]
    y = data[1:-1]
    z = data[2:]
    
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    ax.scatter(x, y, z, alpha=0.6, s=10, color='purple')
    ax.set_title("Test graficzny 3D: Von Neumann ($r_n, r_{n+1}, r_{n+2}$)")
    ax.set_xlabel("$r_n$")
    ax.set_ylabel("$r_{n+1}$")
    ax.set_zlabel("$r_{n+2}$")
    plt.show()
    
samples = von_neumann_generator(seed=1234, n_samples=500)

print(f"Wygenerowano {len(samples)} liczb.")
print(f"Pierwsze dziesięć: {samples[:10]}")

plot_2d_independence(samples)
plot_3d_independence(samples)