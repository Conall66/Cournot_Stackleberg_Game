import numpy as np
import matplotlib.pyplot as plt


betad = 0.5       
beta1 = 0.5       
beta2 = 0.1       


alphad_values = np.linspace(50, 150, 100)  

q1_values = (alphad_values + betad*(beta2 - 2*beta1)) / 2.0
q2_values = (alphad_values - betad*(3*beta2 - 2*beta1)) / 4.0

Q_values = q1_values + q2_values
P_values = (alphad_values - Q_values) / betad
pi1_values = q1_values * (P_values - beta1)
pi2_values = q2_values * (P_values - beta2)


plt.figure(figsize=(12, 5))


plt.subplot(1, 2, 1)
plt.plot(alphad_values, q1_values, label="Leader q1", color="blue")
plt.plot(alphad_values, q2_values, label="Follower q2", color="orange")
plt.xlabel("α₍d₎ (Demand Intercept)")
plt.ylabel("Equilibrium Output")
plt.title("Stackelberg Duopoly: Outputs vs. α₍d₎")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"β₍d₎ = {betad}\nβ₁ = {beta1}\nβ₂ = {beta2}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))


plt.subplot(1, 2, 2)
plt.plot(alphad_values, pi1_values, label="Leader π1", color="green")
plt.plot(alphad_values, pi2_values, label="Follower π2", color="red")
plt.xlabel("α₍d₎ (Demand Intercept)")
plt.ylabel("Equilibrium Profit")
plt.title("Stackelberg Duopoly: Profits vs. α₍d₎")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"β₍d₎ = {betad}\nβ₁ = {beta1}\nβ₂ = {beta2}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
