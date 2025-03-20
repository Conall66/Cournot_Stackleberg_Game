
# Effect of increasing N in Stackelberg environment

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initialise arrays

Q_vals = []
P_vals = []
N = range(2, 11)

for i in N:

    alphad = 360             
    betad  = 2.58

    beta_list = [0.2] * i
    n = len(beta_list)
    beta_leader = beta_list[0]
    S_followers = sum(beta_list[1:])      # Sum of followers' cost parameters

    q1 = (alphad + betad*(S_followers - n*beta_leader)) / 2.0

    q_followers = []
    for i in range(1, n):
        q_i = (alphad + betad*(n*beta_leader + S_followers)) / (2.0 * n) - betad*beta_list[i]
        q_followers.append(q_i)

    Q = q1 + sum(q_followers)
    P = (alphad - Q) / betad

    pi1 = q1 * (P - beta_leader)
    pi_followers = [q_followers[i]*(P - beta_list[i+1]) for i in range(n-1)]

    Q_vals.append(Q)
    P_vals.append(P)

print(Q_vals)
print(P_vals)

# ______________________________________________________________________

fig, ax1 = plt.subplots()

ax1.set_xlabel("Number of Firms (N)")
ax1.set_ylabel("Market Price (P)", color="tab:red")
ax1.plot(N, P_vals, "ro-", label="Price (P)")
ax1.tick_params(axis="y", labelcolor="tab:red")

ax2 = ax1.twinx()
ax2.set_ylabel("Total Quantity (Q)", color="tab:blue")
ax2.plot(N, Q_vals, "bo-", label="Total Quantity (Q)")
ax2.tick_params(axis="y", labelcolor="tab:blue")

plt.title("Effect of Increasing N on Market Price and Quantity")
plt.show()