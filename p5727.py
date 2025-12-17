n = int(input().strip())

nums = []
res = n
while True:
    nums.append(res)
    if res == 1:
        break

    if res % 2 == 0:
        res //= 2
    else:
        res = res * 3 + 1

nums = nums[::-1]
print(*nums)