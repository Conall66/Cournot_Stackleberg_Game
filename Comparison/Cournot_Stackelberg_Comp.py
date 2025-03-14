import numpy as np
import matplotlib.pyplot as plt

alphad = 100.0
betad  = 0.5
beta1  = 0.5
beta2  = 0.1

q1_c = (alphad + betad*(beta2 - 2*beta1)) / 3.0
q2_c = (alphad + betad*(beta1 - 2*beta2)) / 3.0
Q_c  = q1_c + q2_c
P_c  = (alphad - Q_c) / betad
pi1_c = q1_c * (P_c - beta1)
pi2_c = q2_c * (P_c - beta2)

q1_s = (alphad + betad*(beta2 - 2*beta1)) / 2.0
q2_s = (alphad - betad*(3*beta2 - 2*beta1)) / 4.0
Q_s  = q1_s + q2_s
P_s  = (alphad - Q_s) / betad
pi1_s = q1_s * (P_s - beta1)
pi2_s = q2_s * (P_s - beta2)

fig, axs = plt.subplots(1, 3, figsize=(10, 12))

labels_qty = ["Firm 1 Output", "Firm 2 Output", "Total Quantity"]
cournot_qty = [q1_c, q2_c, Q_c]
stackelberg_qty = [q1_s, q2_s, Q_s]
x = np.arange(len(labels_qty))
width = 0.35

axs[0].bar(x - width/2, cournot_qty, width, label="Cournot", color="skyblue")
axs[0].bar(x + width/2, stackelberg_qty, width, label="Stackelberg", color="salmon")
axs[0].set_xticks(x)
axs[0].set_xticklabels(labels_qty)
axs[0].set_ylabel("Quantity")
axs[0].set_title("Equilibrium Quantities")
axs[0].legend()
axs[0].grid(axis="y", linestyle="--", alpha=0.7)
axs[0].text(0.05, 0.90, f"α₍d₎ = {alphad}, β₍d₎ = {betad}\nβ₁ = {beta1}, β₂ = {beta2}",
           transform=axs[0].transAxes, fontsize=10, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

labels_price = ["Market Price"]
cournot_price = [P_c]
stackelberg_price = [P_s]
x2 = np.arange(len(labels_price))

axs[1].bar(x2 - width/2, cournot_price, width, label="Cournot", color="skyblue")
axs[1].bar(x2 + width/2, stackelberg_price, width, label="Stackelberg", color="salmon")
axs[1].set_xticks(x2)
axs[1].set_xticklabels(labels_price)
axs[1].set_ylabel("Price")
axs[1].set_title("Market Price")
axs[1].legend()
axs[1].grid(axis="y", linestyle="--", alpha=0.7)
axs[1].text(0.05, 0.90, f"α₍d₎ = {alphad}, β₍d₎ = {betad}\nβ₁ = {beta1}, β₂ = {beta2}",
           transform=axs[1].transAxes, fontsize=10, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

labels_profit = ["Firm 1 Profit", "Firm 2 Profit"]
cournot_profit = [pi1_c, pi2_c]
stackelberg_profit = [pi1_s, pi2_s]
x3 = np.arange(len(labels_profit))

axs[2].bar(x3 - width/2, cournot_profit, width, label="Cournot", color="skyblue")
axs[2].bar(x3 + width/2, stackelberg_profit, width, label="Stackelberg", color="salmon")
axs[2].set_xticks(x3)
axs[2].set_xticklabels(labels_profit)
axs[2].set_ylabel("Profit")
axs[2].set_title("Profits")
axs[2].legend()
axs[2].grid(axis="y", linestyle="--", alpha=0.7)
axs[2].text(0.05, 0.90, f"α₍d₎ = {alphad}, β₍d₎ = {betad}\nβ₁ = {beta1}, β₂ = {beta2}",
           transform=axs[2].transAxes, fontsize=10, bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5))

plt.suptitle("Comparison of Cournot vs. Stackelberg Duopoly Outcomes")
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
