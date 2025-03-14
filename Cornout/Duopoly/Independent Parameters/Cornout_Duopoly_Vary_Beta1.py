import numpy as np
import matplotlib.pyplot as plt

# Fixed parameters
alphad = 100.0      # Demand intercept
betad  = 0.5        # Demand slope factor
beta2  = 0.1        # Cost parameter for firm 2

# Vary beta1 over a range
beta1_values = np.linspace(0.1, 1.0, 100)  # For example, from 0.1 to 1.0

# Cournot Duopoly formulas:
#   q1 = [alphad + betad*(beta2 - 2*beta1)] / 3
#   q2 = [alphad + betad*(beta1 - 2*beta2)] / 3
#   Q  = q1 + q2
#   P  = (alphad - Q) / betad
#   π1 = q1*(P - beta1)
#   π2 = q2*(P - beta2)

q1_vals = (alphad + betad*(beta2 - 2*beta1_values)) / 3.0
q2_vals = (alphad + betad*(beta1_values - 2*beta2)) / 3.0
Q_vals  = q1_vals + q2_vals
P_vals  = (alphad - Q_vals) / betad
pi1_vals = q1_vals * (P_vals - beta1_values)
pi2_vals = q2_vals * (P_vals - beta2)

plt.figure(figsize=(12, 5))

# Plot quantities vs. beta1
plt.subplot(1, 2, 1)
plt.plot(beta1_values, q1_vals, label='Firm 1 (q1)', color='blue')
plt.plot(beta1_values, q2_vals, label='Firm 2 (q2)', color='orange')
plt.xlabel('β₁ (Cost Parameter for Firm 1)')
plt.ylabel('Equilibrium Quantity')
plt.title('Quantities vs. β₁')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₂ = {beta2}", 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot profits vs. beta1
plt.subplot(1, 2, 2)
plt.plot(beta1_values, pi1_vals, label='Firm 1 Profit (π1)', color='green')
plt.plot(beta1_values, pi2_vals, label='Firm 2 Profit (π2)', color='red')
plt.xlabel('β₁ (Cost Parameter for Firm 1)')
plt.ylabel('Equilibrium Profit')
plt.title('Profits vs. β₁')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₂ = {beta2}", 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
