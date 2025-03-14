import numpy as np
import matplotlib.pyplot as plt

# Fixed parameters
alphad = 100.0    # Demand intercept
beta1  = 0.5      # Leader's cost parameter (firm 1)
beta2  = 0.1      # Follower's cost parameter (firm 2)

# Vary betad over a range
betad_values = np.linspace(0.1, 1.0, 100)

# Stackelberg Duopoly Equilibrium Formulas:
# q1 = [alphad + betad*(beta2 - 2*beta1)] / 2
# q2 = [alphad - betad*(3*beta2 - 2*beta1)] / 4
q1_values = (alphad + betad_values*(beta2 - 2*beta1)) / 2.0
q2_values = (alphad - betad_values*(3*beta2 - 2*beta1)) / 4.0

Q_values = q1_values + q2_values
P_values = (alphad - Q_values) / betad_values
pi1_values = q1_values * (P_values - beta1)
pi2_values = q2_values * (P_values - beta2)

# Plotting
plt.figure(figsize=(12, 5))

# Plot outputs vs. betad
plt.subplot(1, 2, 1)
plt.plot(betad_values, q1_values, label="Leader q1", color="blue")
plt.plot(betad_values, q2_values, label="Follower q2", color="orange")
plt.xlabel("β₍d₎ (Demand Slope Factor)")
plt.ylabel("Equilibrium Output")
plt.title("Stackelberg Duopoly: Outputs vs. β₍d₎")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₁ = {beta1}\nβ₂ = {beta2}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

# Plot profits vs. betad
plt.subplot(1, 2, 2)
plt.plot(betad_values, pi1_values, label="Leader π1", color="green")
plt.plot(betad_values, pi2_values, label="Follower π2", color="red")
plt.xlabel("β₍d₎ (Demand Slope Factor)")
plt.ylabel("Equilibrium Profit")
plt.title("Stackelberg Duopoly: Profits vs. β₍d₎")
plt.legend()
plt.grid(True)
plt.text(0.05, 0.95, f"α₍d₎ = {alphad}\nβ₁ = {beta1}\nβ₂ = {beta2}",
         transform=plt.gca().transAxes, fontsize=10, verticalalignment='top',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.show()
