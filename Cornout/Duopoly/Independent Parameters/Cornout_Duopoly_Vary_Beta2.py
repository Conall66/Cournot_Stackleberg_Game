import numpy as np
import matplotlib.pyplot as plt


alphad = 100.0      
betad  = 0.5        
beta1  = 0.5       

beta2_values = np.linspace(0.1, 1.0, 100)  


q1_vals = (alphad + betad*(beta2_values - 2*beta1)) / 3.0
q2_vals = (alphad + betad*(beta1 - 2*beta2_values)) / 3.0
Q_vals  = q1_vals + q2_vals
P_vals  = (alphad - Q_vals) / betad
pi1_vals = q1_vals * (P_vals - beta1)
pi2_vals = q2_vals * (P_vals - beta2_values)

plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(beta2_values, q1_vals, label='Firm 1 (q1)', color='blue')
plt.plot(beta2_values, q2_vals, label='Firm 2 (q2)', color='orange')
plt.xlabel('β₂ (Cost Parameter for Firm 2)')
plt.ylabel('Equilibrium Quantity')
plt.title('Quantities vs. β₂')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₁ = {beta1}", 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.subplot(1, 2, 2)
plt.plot(beta2_values, pi1_vals, label='Firm 1 Profit (π1)', color='green')
plt.plot(beta2_values, pi2_vals, label='Firm 2 Profit (π2)', color='red')
plt.xlabel('β₂ (Cost Parameter for Firm 2)')
plt.ylabel('Equilibrium Profit')
plt.title('Profits vs. β₂')
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₁ = {beta1}", 
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
