import matplotlib.pyplot as plt
import numpy as np

print("\n1.Znalezienie stałej c:")
print("X(Ω) = {1, 2, 3, 4}")
print("P(X = i) = i·c")
print("\nWarunek: suma wszystkich prawdopodobieństw = 1")
print("P(X=1) + P(X=2) + P(X=3) + P(X=4) = 1")
print("1·c + 2·c + 3·c + 4·c = 1")
print("10·c = 1\n")

c = 1/10
print(f"\033[1mStała c:\033[0m {c} \n")
values = [1, 2, 3, 4]
probabilities = [i * c for i in values]

print(f"P(X=1) = 1·{c} = {probabilities[0]}")
print(f"P(X=2) = 2·{c} = {probabilities[1]}")
print(f"P(X=3) = 3·{c} = {probabilities[2]}")
print(f"P(X=4) = 4·{c} = {probabilities[3]} \n")
print(f"\033[1mSuma:\033[0m {sum(probabilities)} \n")

print("Metoda 1: Bezpośrednie sumowanie")
print("P(2 ≤ X ≤ 3) = P(X=2) + P(X=3)")
print(f"= 2·c + 3·c")
print(f"= 2·{c} + 3·{c}")
print(f"= {2*c} + {3*c}")

result_method1 = probabilities[1] + probabilities[2]
print(f"\033[1m= {result_method1} \033[0m\n")

print("Metoda 2: Przez sumowanie zdań 2 i 3 z definicji")
print("P(2 ≤ X ≤ 3) = Σ P(X=i) dla i ∈ {2, 3}")

result_method2 = sum(probabilities[i-1] for i in [2, 3])
print(f"= {probabilities[1]} + {probabilities[2]}")

print(f"\033[1m= {result_method2} \033[0m\n")

print("Weryfikacaja zgodności wyników:")
print(f"\033[1mMetoda 1: {result_method1}\033[0m")
print(f"\033[1mMetoda 2: {result_method2}\033[0m")
print(f"\033[1mZgodność: {'Tak' if abs(result_method1 - result_method2) < 1e-10 else 'Nie'}\033[0m\n")

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax1 = axes[0]
colors = ['lightblue', 'salmon', 'salmon', 'lightblue']
bars = ax1.bar(values, probabilities, color=colors, edgecolor='black', linewidth=2, width=0.6)

bars[1].set_color('salmon')
bars[2].set_color('salmon')

ax1.set_xlabel('X', fontsize=12, fontweight='bold')
ax1.set_ylabel('P(X = i)', fontsize=12, fontweight='bold')
ax1.set_title('Rozkład zmiennej losowej X', fontsize=13, fontweight='bold')
ax1.set_xticks(values)
ax1.grid(axis='y', alpha=0.3, linestyle='--')
ax1.set_ylim([0, max(probabilities) * 1.2])

for i, (val, prob) in enumerate(zip(values, probabilities)):
    ax1.text(val, prob + 0.01, f'{prob:.1f}', ha='center', fontsize=11, fontweight='bold')

ax1.text(0.5, 0.95, 'Kolor jasnoniebieski: nie wliczone do P(2 ≤ X ≤ 3)', 
         transform=ax1.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
ax1.text(0.5, 0.85, 'Kolor łososiowy: wliczone do P(2 ≤ X ≤ 3)', 
         transform=ax1.transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='salmon', alpha=0.5))

ax2 = axes[1]
cumulative_probs = np.cumsum(probabilities)
x_cdf = [0] + values
y_cdf = [0] + list(cumulative_probs)

ax2.step(x_cdf, y_cdf, 'b-', linewidth=2, marker='o', markersize=8, where='post', label='F(x) = P(X ≤ x)')
ax2.fill_between([1.99, 3.01], 0, 1, alpha=0.3, color='salmon', label='P(2 ≤ X ≤ 3)')

ax2.set_xlabel('X', fontsize=12, fontweight='bold')
ax2.set_ylabel('F(X)', fontsize=12, fontweight='bold')
ax2.set_title('Dystrybuanta zmiennej losowej X', fontsize=13, fontweight='bold')
ax2.grid(True, alpha=0.3, linestyle='--')
ax2.set_xlim([-0.5, 5])
ax2.set_ylim([-0.05, 1.1])
ax2.legend(fontsize=10)

for i, cum_prob in enumerate(cumulative_probs):
    ax2.text(x_cdf[i], cum_prob + 0.05, f'{cum_prob:.2f}', ha='center', fontsize=9)

plt.tight_layout()
print("\nWizualizacja zapisana do: zad2_lista0_visualization.png \n")
plt.show()

print(f"\033[1mPodsumowanie:\033[0m")
print(f"P(2 ≤ X ≤ 3) = {result_method1} = {result_method1.as_integer_ratio()[0]}/{result_method1.as_integer_ratio()[1]} = 50%")