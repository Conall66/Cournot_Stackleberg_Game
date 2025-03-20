# Input parameters

alphad = 360             
betad  = 2.58             
beta_list = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2]

n = len(beta_list)
sum_beta = sum(beta_list)

q = []  
for i in range(n):
    q_i = alphad/(n+1) + betad * ((sum_beta)/(n+1) - beta_list[i])
    q.append(q_i)

Q = sum(q)
P = (alphad - Q) / betad

pi = [q[i]*(P - beta_list[i]) for i in range(n)]

print("Cournot Oligopoly:")
for i in range(n):
    print(f"Firm {i+1} output, q_{i+1} = {q[i]:.4f}, profit, π_{i+1} = {pi[i]:.4f}")
print(f"Total quantity, Q = {Q:.4f}")
print(f"Market price, P = {P:.4f}")