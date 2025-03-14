# Cournot Duopoly
alphad = 100.0      # Demand intercept
betad  = 0.5        # Demand slope factor
beta1  = 0.5        # Cost parameter for firm 1
beta2  = 0.1        # Cost parameter for firm 2

q1 = (alphad + betad*(beta2 - 2*beta1)) / 3.0
q2 = (alphad + betad*(beta1 - 2*beta2)) / 3.0
Q  = q1 + q2
P  = (alphad - Q) / betad
pi1 = q1 * (P - beta1)
pi2 = q2 * (P - beta2)

print("Cournot Duopoly:")
print(f"Firm 1 output, q1 = {q1:.4f}")
print(f"Firm 2 output, q2 = {q2:.4f}")
print(f"Total quantity, Q = {Q:.4f}")
print(f"Market price, P = {P:.4f}")
print(f"Firm 1 profit, π1 = {pi1:.4f}")
print(f"Firm 2 profit, π2 = {pi2:.4f}")
