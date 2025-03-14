import numpy as np
import matplotlib.pyplot as plt

alphad = 100.0
betad  = 0.5
beta1  = 0.5
beta2  = 0.1

q1_range = np.linspace(0, alphad/2, 100)
BR_follower = (alphad - q1_range - betad * beta2) / 2.0


q1_star = (alphad + betad * (beta2 - 2 * beta1)) / 2.0

q2_star = (alphad - q1_star - betad * beta2) / 2.0

plt.figure(figsize=(8, 6))
plt.plot(q1_range, BR_follower, label="Follower's Best Response", color="blue")
plt.axvline(x=q1_star, color="red", linestyle="--", label="Leader's Equilibrium Output")
plt.scatter([q1_star], [q2_star], color="green", zorder=5, label="Nash Equilibrium")
plt.text(q1_star, q2_star, f"  NE: ({q1_star:.2f}, {q2_star:.2f})", color="green", fontsize=10)
plt.xlabel(r"$q_1$ (Leader Output)")
plt.ylabel(r"$q_2$ (Follower Output)")
plt.title("Stackelberg Duopoly: Leader and Follower")
plt.legend()
plt.grid(True)
plt.xlim(0, alphad)
plt.ylim(0, alphad)
plt.show()
