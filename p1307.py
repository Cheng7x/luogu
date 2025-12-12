n = int(input().strip())
flag = False
if n < 0:
    n = abs(n)
    flag = True
n = int(str(n)[::-1])
if flag == True:
    n = -n
print(n)