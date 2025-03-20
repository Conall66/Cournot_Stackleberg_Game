alphad = 360             
betad  = 2.58             
beta_list = [0.28, 0.12, 0.2, 0.22, 0.25]

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

print("Stackelberg Oligopoly:")
print(f"Leader (Firm 1) output, q1 = {q1:.4f}, profit, π1 = {pi1:.4f}")
for i in range(1, n):
    print(f"Follower (Firm {i+1}) output, q_{i+1} = {q_followers[i-1]:.4f}, profit, π_{i+1} = {pi_followers[i-1]:.4f}")
print(f"Total quantity, Q = {Q:.4f}")
print(f"Market price, P = {P:.4f}")