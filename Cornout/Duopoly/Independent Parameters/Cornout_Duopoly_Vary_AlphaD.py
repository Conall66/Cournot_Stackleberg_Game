import numpy as np
import matplotlib.pyplot as plt

# Parameters
betad = 0.5       # Demand slope factor
beta1 = 0.5       # Cost parameter for firm 1
beta2 = 0.1       # Cost parameter for firm 2

# Range for alpha_d
alphad_values = np.linspace(10, 200, 100)

# Equilibrium quantities
q1_values = (alphad_values + betad*(beta2 - 2*beta1)) / 3.0
q2_values = (alphad_values + betad*(beta1 - 2*beta2)) / 3.0

# Total quantity and price
Q_values = q1_values + q2_values
P_values = (alphad_values - Q_values) / betad

# Profits
pi1_values = q1_values * (P_values - beta1)
pi2_values = q2_values * (P_values - beta2)

#############################################################################
# FIGURE 1
#############################################################################
plt.figure(figsize=(10, 4))

# Subplot 1: q1 and q2
plt.subplot(1, 2, 1)
plt.plot(alphad_values, q1_values, label='q1')
plt.plot(alphad_values, q2_values, label='q2')
plt.xlabel('αd (Demand Intercept)')
plt.ylabel('Quantity')
plt.title('Equilibrium Quantities vs. αd')
plt.legend()
plt.grid(True)

# Subplot 2: pi1 and pi2
plt.subplot(1, 2, 2)
plt.plot(alphad_values, pi1_values, label='π1')
plt.plot(alphad_values, pi2_values, label='π2')
plt.xlabel('αd (Demand Intercept)')
plt.ylabel('Profit')
plt.title('Equilibrium Profits vs. αd')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()

#############################################################################
# FIGURE 2
#############################################################################
plt.figure(figsize=(10, 4))

# Subplot 1: Total Quantity Q
plt.subplot(1, 2, 1)
plt.plot(alphad_values, Q_values, label='Q')
plt.xlabel('αd (Demand Intercept)')
plt.ylabel('Total Quantity')
plt.title('Total Quantity vs. αd')
plt.grid(True)

# Subplot 2: Price P
plt.subplot(1, 2, 2)
plt.plot(alphad_values, P_values, label='P')
plt.xlabel('αd (Demand Intercept)')
plt.ylabel('Price')
plt.title('Price vs. αd')
plt.grid(True)

plt.tight_layout()
plt.show()
