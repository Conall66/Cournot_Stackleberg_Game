import numpy as np
import matplotlib.pyplot as plt

# Fixed parameters
alphad = 100.0    # Demand intercept
betad  = 0.5      # Demand slope factor
beta1  = 0.5      # Leader's cost parameter (firm 1)

# Vary beta2 over a range
beta2_values = np.linspace(0.1, 1.0, 100)

# Stackelberg Duopoly Equilibrium Formulas:
# q1 = [alphad + betad*(beta2 - 2*beta1)] / 2
# q2 = [alphad - betad*(3*beta2 - 2*beta1)] / 4
q1_values = (alphad + betad*(beta2_values - 2*beta1)) / 2.0
q2_values = (alphad - betad*(3*beta2_values - 2*beta1)) / 4.0

Q_values = q1_values + q2_values
P_values = (alphad - Q_values) / betad
pi1_values = q1_values * (P_values - beta1)
pi2_values = q2_values * (P_values - beta2_values)

# Plotting
plt.figure(figsize=(12, 5))

# Plot outputs vs. beta2
plt.subplot(1, 2, 1)
plt.plot(beta2_values, q1_values, label="Leader q1", color="blue")
plt.plot(beta2_values, q2_values, label="Follower q2", color="orange")
plt.xlabel("β₂ (Follower's Cost Parameter)")
plt.ylabel("Equilibrium Output")
plt.title("Stackelberg Duopoly: Outputs vs. β₂")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₁ = {beta1}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot profits vs. beta2
plt.subplot(1, 2, 2)
plt.plot(beta2_values, pi1_values, label="Leader π1", color="green")
plt.plot(beta2_values, pi2_values, label="Follower π2", color="red")
plt.xlabel("β₂ (Follower's Cost Parameter)")
plt.ylabel("Equilibrium Profit")
plt.title("Stackelberg Duopoly: Profits vs. β₂")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₁ = {beta1}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
