import numpy as np
import matplotlib.pyplot as plt


alphad = 100.0    
betad  = 0.5      
beta2  = 0.1      


beta1_values = np.linspace(0.1, 20, 100)

q1_values = (alphad + betad*(beta2 - 2*beta1_values)) / 2.0
q2_values = (alphad - betad*(3*beta2 - 2*beta1_values)) / 4.0

Q_values = q1_values + q2_values
P_values = (alphad - Q_values) / betad
pi1_values = q1_values * (P_values - beta1_values)
pi2_values = q2_values * (P_values - beta2)


plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(beta1_values, q1_values, label="Leader q1", color="blue")
plt.plot(beta1_values, q2_values, label="Follower q2", color="orange")
plt.xlabel("β₁ (Leader's Cost Parameter)")
plt.ylabel("Equilibrium Output")
plt.title("Stackelberg Duopoly: Outputs vs. β₁")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₂ = {beta2}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.subplot(1, 2, 2)
plt.plot(beta1_values, pi1_values, label="Leader π1", color="green")
plt.plot(beta1_values, pi2_values, label="Follower π2", color="red")
plt.xlabel("β₁ (Leader's Cost Parameter)")
plt.ylabel("Equilibrium Profit")
plt.title("Stackelberg Duopoly: Profits vs. β₁")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₍d₎ = {betad}\nβ₂ = {beta2}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
