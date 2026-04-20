import matplotlib.pyplot as plt
import numpy as np

class LehmerRNG:
    def __init__(self, seed=1):
        self.state = seed
        self.a = 16807
        self.m = 2**31 - 1 # liczba pierwsza mersenne'a

    def next_float(self):
        self.state = (self.a * self.state) % self.m
        return self.state / self.m

def monte_carlo_pi_visualization(n_points=10000):
    rng = LehmerRNG(seed=12345)
    
    x_inside = []
    y_inside = []
    x_outside = []
    y_outside = []

    inside_count = 0

    for _ in range(n_points):
        x = rng.next_float()
        y = rng.next_float()
        
        if x**2 + y**2 <= 1.0:
            inside_count += 1
            x_inside.append(x)
            y_inside.append(y)
        else:
            x_outside.append(x)
            y_outside.append(y)

    pi_estimate = 4 * inside_count / n_points

    plt.figure(figsize=(8, 8))
    
    plt.scatter(x_inside, y_inside, color='blue', s=5, alpha=0.6, label='Wewnątrz koła')
    plt.scatter(x_outside, y_outside, color='red', s=5, alpha=0.6, label='Na zewnątrz koła')
    circle_x = np.linspace(0, 1, 200)
    circle_y = np.sqrt(1 - circle_x**2)
    
    plt.plot(circle_x, circle_y, color='black', linewidth=2, label='Okrąg $x^2+y^2=1$')
    plt.title(f'Aproksymacja π metodą Monte Carlo (Generator Lehmera)\nN = {n_points}, Wyznaczone π ≈ {pi_estimate:.5f}', fontsize=14)
    
    plt.xlabel('x', fontsize=12)
    plt.ylabel('y', fontsize=12)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    
    plt.gca().set_aspect('equal', adjustable='box')
    plt.legend(loc='upper right')
    plt.grid(True, linestyle='--', alpha=0.7)
        
    plt.show()
    
    return pi_estimate

estimated_pi = monte_carlo_pi_visualization(10000)
print(f"Wyznaczone przybliżenie pi: {estimated_pi}")