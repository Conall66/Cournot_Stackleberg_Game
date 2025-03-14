import numpy as np
import matplotlib.pyplot as plt

alphad = 100.0      
betad  = 0.5       
beta2  = 0.1        
beta1_values = np.linspace(0.1, 1.0, 100) 


q1_vals = (alphad + betad*(beta2 - 2*beta1_values)) / 3.0
q2_vals = (alphad + betad*(beta1_values - 2*beta2)) / 3.0
Q_vals  = q1_vals + q2_vals
P_vals  = (alphad - Q_vals) / betad
pi1_vals = q1_vals * (P_vals - beta1_values)
pi2_vals = q2_vals * (P_vals - beta2)

plt.figure(figsize=(12, 5))
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
