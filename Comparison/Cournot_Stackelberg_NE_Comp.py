import numpy as np
import matplotlib.pyplot as plt

# Input Parameters
alphad = 100.0
betad  = 0.5
beta1  = 0.5
beta2  = 0.1

# Create range for q1 values
q1_range = np.linspace(0, alphad, 100)

# Cournot best response functions
BR2 = (alphad - q1_range - betad * beta2) / 2.0
BR1 = alphad - betad * beta1 - 2 * q1_range

# Equilibrium values
# Cournot equilibrium
q1_cournot = (alphad + betad * (beta2 - 2 * beta1)) / 3.0
q2_cournot = (alphad + betad * (beta1 - 2 * beta2)) / 3.0
# Stackelberg equilibrium
q1_stack = (alphad + betad * (beta2 - 2 * beta1)) / 2.0
q2_stack = (alphad - betad * (3 * beta2 - 2 * beta1)) / 4.0

plt.figure(figsize=(8, 6))
plt.plot(q1_range, BR1, label="Firm 1 Best Response (Cournot)", color="red")
plt.plot(q1_range, BR2, label="Firm 2 Best Response (Cournot)", color="blue")
plt.scatter([q1_cournot], [q2_cournot], color="green", zorder=5, label="Cournot Equilibrium")
plt.text(q1_cournot, q2_cournot, f"  Cournot NE: ({q1_cournot:.2f}, {q2_cournot:.2f})", color="green", fontsize=15)
plt.scatter([q1_stack], [q2_stack], color="purple", zorder=5, label="Stackelberg Equilibrium")
plt.text(q1_stack, q2_stack, f"  Stackelberg NE: ({q1_stack:.2f}, {q2_stack:.2f})", color="purple", fontsize=15)

plt.xlabel(r"$q_1$ (Firm 1 Output)")
plt.ylabel(r"$q_2$ (Firm 2 Output)")
plt.title("Cournot Best Response Curves with Stackelberg Equilibrium")
plt.legend()
plt.grid(True)
plt.xlim(0, alphad)
plt.ylim(0, alphad)

# Annotate parameter values on the plot (using axes fraction coordinates)
params_text = f"$\\alpha_d$ = {alphad}, $\\beta_d$ = {betad}\n$\\beta_1$ = {beta1}, $\\beta_2$ = {beta2}"
plt.text(0.05, 0.05, params_text, transform=plt.gca().transAxes,
         fontsize=10, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

plt.show()
