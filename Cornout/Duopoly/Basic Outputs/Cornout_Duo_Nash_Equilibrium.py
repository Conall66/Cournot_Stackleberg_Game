import numpy as np
import matplotlib.pyplot as plt

alphad = 100.0
betad  = 0.5
beta1  = 0.5
beta2  = 0.1

q1_range = np.linspace(0, alphad/2, 100)
BR2 = (alphad - q1_range - betad * beta2) / 2.0
BR1 = alphad - betad * beta1 - 2 * q1_range

q1_star = (alphad + betad * (beta2 - 2 * beta1)) / 3.0
q2_star = (alphad + betad * (beta1 - 2 * beta2)) / 3.0

plt.figure(figsize=(8, 6))
plt.plot(q1_range, BR1, label="Firm 1 Best Response", color="red")
plt.plot(q1_range, BR2, label="Firm 2 Best Response", color="blue")
plt.scatter([q1_star], [q2_star], color="green", zorder=5, label="Nash Equilibrium")
plt.text(q1_star, q2_star, f"  NE: ({q1_star:.2f}, {q2_star:.2f})", color="green", fontsize=10)
plt.xlabel(r"$q_1$ (Firm 1 Output)")
plt.ylabel(r"$q_2$ (Firm 2 Output)")
plt.title("Best Response Curves in Cournot Duopoly")
plt.legend()
plt.grid(True)
plt.xlim(0, alphad/2)
plt.ylim(0, alphad/2)
plt.show()
