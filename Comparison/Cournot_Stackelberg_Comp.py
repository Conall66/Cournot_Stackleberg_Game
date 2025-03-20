import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# ---------- 1) Define a function to compute Cournot & Stackelberg outcomes ----------
def compute_equilibria(alphad, betad, beta1, beta2):
    # Cournot
    q1_c = (alphad + betad*(beta2 - 2*beta1)) / 3.0
    q2_c = (alphad + betad*(beta1 - 2*beta2)) / 3.0
    Q_c  = q1_c + q2_c
    P_c  = (alphad - Q_c) / betad
    pi1_c = q1_c * (P_c - beta1)
    pi2_c = q2_c * (P_c - beta2)

    # Stackelberg
    q1_s = (alphad + betad*(beta2 - 2*beta1)) / 2.0
    q2_s = (alphad - betad*(3*beta2 - 2*beta1)) / 4.0
    Q_s  = q1_s + q2_s
    P_s  = (alphad - Q_s) / betad
    pi1_s = q1_s * (P_s - beta1)
    pi2_s = q2_s * (P_s - beta2)

    return (q1_c, q2_c, Q_c, P_c, pi1_c, pi2_c,
            q1_s, q2_s, Q_s, P_s, pi1_s, pi2_s)

# ---------- 2) Initial parameter values ----------
alphad0 = 100.0
betad0  = 0.5
beta10  = 0.5
beta20  = 0.1

# ---------- 3) Create main figure and subplots ----------
fig, axs = plt.subplots(1, 3, figsize=(10, 5))
plt.subplots_adjust(bottom=0.3)  # Make space at the bottom for sliders

# Compute initial values
(q1_c, q2_c, Q_c, P_c, pi1_c, pi2_c,
 q1_s, q2_s, Q_s, P_s, pi1_s, pi2_s) = compute_equilibria(alphad0, betad0, beta10, beta20)

# ---------- 4) Plot for Equilibrium Quantities ----------
labels_qty = ["Firm 1 Output", "Firm 2 Output", "Total Quantity"]
cournot_qty = [q1_c, q2_c, Q_c]
stackelberg_qty = [q1_s, q2_s, Q_s]
x_qty = np.arange(len(labels_qty))
width = 0.35

bar_cournot_qty = axs[0].bar(x_qty - width/2, cournot_qty, width, label="Cournot", color="skyblue")
bar_stackelberg_qty = axs[0].bar(x_qty + width/2, stackelberg_qty, width, label="Stackelberg", color="salmon")
axs[0].set_xticks(x_qty)
axs[0].set_xticklabels(labels_qty)
axs[0].set_ylabel("Quantity")
axs[0].set_title("Equilibrium Quantities")
axs[0].legend()
axs[0].grid(axis="y", linestyle="--", alpha=0.7)
text_qty = axs[0].text(
    0.05, 0.90,
    f"α(d) = {alphad0}, β(d) = {betad0}\nβ1 = {beta10}, β2 = {beta20}",
    transform=axs[0].transAxes, fontsize=8,
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5)
)

# ---------- 5) Plot for Market Price ----------
labels_price = ["Market Price"]
cournot_price = [P_c]
stackelberg_price = [P_s]
x_price = np.arange(len(labels_price))

bar_cournot_price = axs[1].bar(x_price - width/2, cournot_price, width, label="Cournot", color="skyblue")
bar_stackelberg_price = axs[1].bar(x_price + width/2, stackelberg_price, width, label="Stackelberg", color="salmon")
axs[1].set_xticks(x_price)
axs[1].set_xticklabels(labels_price)
axs[1].set_ylabel("Price")
axs[1].set_title("Market Price")
axs[1].legend()
axs[1].grid(axis="y", linestyle="--", alpha=0.7)
text_price = axs[1].text(
    0.05, 0.90,
    f"α(d) = {alphad0}, β(d) = {betad0}\nβ1 = {beta10}, β2 = {beta20}",
    transform=axs[1].transAxes, fontsize=8,
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5)
)

# ---------- 6) Plot for Profits ----------
labels_profit = ["Firm 1 Profit", "Firm 2 Profit"]
cournot_profit = [pi1_c, pi2_c]
stackelberg_profit = [pi1_s, pi2_s]
x_profit = np.arange(len(labels_profit))

bar_cournot_profit = axs[2].bar(x_profit - width/2, cournot_profit, width, label="Cournot", color="skyblue")
bar_stackelberg_profit = axs[2].bar(x_profit + width/2, stackelberg_profit, width, label="Stackelberg", color="salmon")
axs[2].set_xticks(x_profit)
axs[2].set_xticklabels(labels_profit)
axs[2].set_ylabel("Profit")
axs[2].set_title("Profits")
axs[2].legend()
axs[2].grid(axis="y", linestyle="--", alpha=0.7)
text_profit = axs[2].text(
    0.05, 0.90,
    f"α(d) = {alphad0}, β(d) = {betad0}\nβ1 = {beta10}, β2 = {beta20}",
    transform=axs[2].transAxes, fontsize=8,
    bbox=dict(boxstyle="round", facecolor="wheat", alpha=0.5)
)

plt.suptitle("Comparison of Cournot vs. Stackelberg Duopoly Outcomes")

# ---------- 7) Create Slider Axes ----------
axcolor = 'lightgoldenrodyellow'
# [left, bottom, width, height] in figure coordinates
ax_alpha = plt.axes([0.15, 0.16, 0.7, 0.03], facecolor=axcolor)
ax_beta  = plt.axes([0.15, 0.12, 0.7, 0.03], facecolor=axcolor)
ax_b1    = plt.axes([0.15, 0.08, 0.7, 0.03], facecolor=axcolor)
ax_b2    = plt.axes([0.15, 0.04, 0.7, 0.03], facecolor=axcolor)

slider_alpha = Slider(ax_alpha,  r'$\alpha_d$',  0.0, 200.0, valinit=alphad0, valstep=1.0)
slider_beta  = Slider(ax_beta,   r'$\beta_d$',   0.01, 20.0,   valinit=betad0,  valstep=0.01)
slider_b1    = Slider(ax_b1,     r'$\beta_1$',   0.0,  20.0,   valinit=beta10,  valstep=0.05)
slider_b2    = Slider(ax_b2,     r'$\beta_2$',   0.0,  20.0,   valinit=beta20,  valstep=0.05)

# ---------- 8) Define the Update Function ----------
def update(val):
    # Retrieve current slider values
    a_val = slider_alpha.val
    b_val = slider_beta.val
    b1_val = slider_b1.val
    b2_val = slider_b2.val
    
    # Recompute equilibria
    (q1_c, q2_c, Q_c, P_c, pi1_c, pi2_c,
     q1_s, q2_s, Q_s, P_s, pi1_s, pi2_s) = compute_equilibria(a_val, b_val, b1_val, b2_val)
    
    # Update bar heights for Quantities
    new_cournot_qty = [q1_c, q2_c, Q_c]
    new_stackelberg_qty = [q1_s, q2_s, Q_s]
    for i, bar in enumerate(bar_cournot_qty):
        bar.set_height(new_cournot_qty[i])
    for i, bar in enumerate(bar_stackelberg_qty):
        bar.set_height(new_stackelberg_qty[i])
    
    # Update bar heights for Price
    for i, bar in enumerate(bar_cournot_price):
        bar.set_height([P_c][i])
    for i, bar in enumerate(bar_stackelberg_price):
        bar.set_height([P_s][i])
    
    # Update bar heights for Profits
    new_cournot_profit = [pi1_c, pi2_c]
    new_stackelberg_profit = [pi1_s, pi2_s]
    for i, bar in enumerate(bar_cournot_profit):
        bar.set_height(new_cournot_profit[i])
    for i, bar in enumerate(bar_stackelberg_profit):
        bar.set_height(new_stackelberg_profit[i])
    
    # Update text annotations
    text_string = f"α(d) = {a_val:.2f}, β(d) = {b_val:.2f}\nβ1 = {b1_val:.2f}, β2 = {b2_val:.2f}"
    text_qty.set_text(text_string)
    text_price.set_text(text_string)
    text_profit.set_text(text_string)
    
    # Redraw
    fig.canvas.draw_idle()

# ---------- 9) Attach the 'update' function to each slider ----------
slider_alpha.on_changed(update)
slider_beta.on_changed(update)
slider_b1.on_changed(update)
slider_b2.on_changed(update)

plt.show()
