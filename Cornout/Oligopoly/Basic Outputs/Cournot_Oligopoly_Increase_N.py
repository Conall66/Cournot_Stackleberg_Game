
# Model increase in N oligopoly Cournot
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Initialise arrays

Q_vals = []
P_vals = []
N = range(2, 10)

for i in N:

    alphad = 360             
    betad  = 2.58             
    beta_list = [0.2] * i

    n = len(beta_list)
    sum_beta = sum(beta_list)

    q = []  
    for i in range(n):
        q_i = alphad/(n+1) + betad * ((sum_beta)/(n+1) - beta_list[i])
        q.append(q_i)

    Q = sum(q)
    P = (alphad - Q) / betad

    pi = [q[i]*(P - beta_list[i]) for i in range(n)]

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