import numpy as np
import matplotlib.pyplot as plt

# Parameters
alphad = 100.0
betad  = 0.5

# Create a grid of beta1, beta2 values
beta1_values = np.linspace(0.1, 20, 50)
beta2_values = np.linspace(0.1, 20, 50)
B1, B2 = np.meshgrid(beta1_values, beta2_values)

# Compute q1, q2, and profits over the grid
q1 = (alphad + betad*(B2 - 2*B1)) / 3.0
q2 = (alphad + betad*(B1 - 2*B2)) / 3.0

# Inverse demand
Q  = q1 + q2
P  = (alphad - Q) / betad

# Profits
pi1 = q1 * (P - B1)
pi2 = q2 * (P - B2)

# Set up the figure with two subplots side by side
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# ---- Heatmap for Firm 1 Profit ----
cont1 = ax1.contourf(B1, B2, pi1, levels=50)  # choose how many "levels" of color
cbar1 = fig.colorbar(cont1, ax=ax1)
ax1.set_title('Firm 1 Profit (π₁)')
ax1.set_xlabel('β₁')
ax1.set_ylabel('β₂')
cbar1.set_label('Profit π₁')

# ---- Heatmap for Firm 2 Profit ----
cont2 = ax2.contourf(B1, B2, pi2, levels=50)
cbar2 = fig.colorbar(cont2, ax=ax2)
ax2.set_title('Firm 2 Profit (π₂)')
ax2.set_xlabel('β₁')
ax2.set_ylabel('β₂')
cbar2.set_label('Profit π₂')

plt.tight_layout()
plt.show()
