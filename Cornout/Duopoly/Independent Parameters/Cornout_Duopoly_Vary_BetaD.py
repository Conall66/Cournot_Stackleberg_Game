import numpy as np
import matplotlib.pyplot as plt

# Fixed parameters
alphad = 100.0      # Demand intercept
beta1  = 0.5        # Cost parameter for firm 1
beta2  = 0.1        # Cost parameter for firm 2

# Vary betad over a range
betad_values = np.linspace(0.1, 1.0, 100)  # For example, from 0.1 to 1.0

q1_vals = (alphad + betad_values*(beta2 - 2*beta1)) / 3.0
q2_vals = (alphad + betad_values*(beta1 - 2*beta2)) / 3.0
Q_vals  = q1_vals + q2_vals
P_vals  = (alphad - Q_vals) / betad_values
pi1_vals = q1_vals * (P_vals - beta1)
pi2_vals = q2_vals * (P_vals - beta2)

plt.figure(figsize=(12, 5))

# Plot quantities vs. betad
plt.subplot(1, 2, 1)
plt.plot(betad_values, q1_vals, label='Firm 1 (q1)', color='blue')
plt.plot(betad_values, q2_vals, label='Firm 2 (q2)', color='orange')
plt.xlabel('β₍d₎ (Demand Slope Factor)')
plt.ylabel('Equilibrium Quantity')
plt.title('Quantities vs. β₍d₎')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₁ = {beta1}\nβ₂ = {beta2}", 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot profits vs. betad
plt.subplot(1, 2, 2)
plt.plot(betad_values, pi1_vals, label='Firm 1 Profit (π1)', color='green')
plt.plot(betad_values, pi2_vals, label='Firm 2 Profit (π2)', color='red')
plt.xlabel('β₍d₎ (Demand Slope Factor)')
plt.ylabel('Equilibrium Profit')
plt.title('Profits vs. β₍d₎')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₁ = {beta1}\nβ₂ = {beta2}", 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
