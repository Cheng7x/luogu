n = int(input().strip())
NMAX = 10000
is_prime = [True] * (NMAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(NMAX**0.5) + 1):
    if is_prime[i]:
        for j in range(i*i, NMAX+1, i):
            is_prime[j] = False
         
for i in range(4, n + 1, 2):
    for j in range(2, n//2 + 1):
        if is_prime[j] and is_prime[i - j]:
            print(f"{i}={j}+{i-j}")
            break
