import numpy as np
import matplotlib.pyplot as plt


betad = 0.5       # Demand slope factor
beta1 = 0.5       # Cost parameter for firm 1
beta2 = 0.1       # Cost parameter for firm 2

alphad_values = np.linspace(10, 200, 100)  # For example, from 50 to 150
q1_values = (alphad_values + betad*(beta2 - 2*beta1)) / 3.0
q2_values = (alphad_values + betad*(beta1 - 2*beta2)) / 3.0
Q_values = q1_values + q2_values
P_values = (alphad_values - Q_values) / betad
pi1_values = q1_values * (P_values - beta1)
pi2_values = q2_values * (P_values - beta2)


plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(alphad_values, q1_values, label='Firm 1 (q1)', color='blue')
plt.plot(alphad_values, q2_values, label='Firm 2 (q2)', color='orange')
plt.xlabel('α₍d₎ (Demand Intercept)')
plt.ylabel('Equilibrium Quantity')
plt.title('Equilibrium Quantities vs. α₍d₎')
plt.legend()
plt.grid(True)

plt.text(0.05, 0.95, f'β₁ = {beta1}, β₂ = {beta2}, βd = {betad}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))


plt.subplot(1, 2, 2)
plt.plot(alphad_values, pi1_values, label='Firm 1 Profit (π1)', color='green')
plt.plot(alphad_values, pi2_values, label='Firm 2 Profit (π2)', color='red')
plt.xlabel('α₍d₎ (Demand Intercept)')
plt.ylabel('Equilibrium Profit')
plt.title('Equilibrium Profits vs. α₍d₎')
plt.legend()
plt.grid(True)

plt.text(0.05, 0.95, f'β₁ = {beta1}, β₂ = {beta2}, βd = {betad}', transform=plt.gca().transAxes,
         fontsize=10, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
