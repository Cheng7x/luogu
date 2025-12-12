"""n = int(input().strip())
nums = list(map(int, input().strip().split()))

for idx, num in enumerate(nums, 1):
    print(f"num[{idx}] = {num}")"""

xlist = [1, 1, 2, 3, 3, 3, 4, 5, 6, 11, 10, 10, 8, 7, 6]

"""x=eval(input())
while x!=0:
    xlist.append(x)
    x=eval(input())"""
# 代码开始
seen = set()
result = []
for x in xlist:
    if x not in seen:
        seen.add(x)
        result.append(x)
# 代码结束
print(result)
