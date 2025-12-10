n = int(input().strip())

def factorial(n):
    term = 1
    s = 1
    while term < n:
        term += 1
        s *= term
    return s

out = 0
for i in range(1, n + 1):
    out += factorial(i)
print(out)