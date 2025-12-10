height = list(map(int, input().split()))
reach = int(input().strip())

count = 0
for i in height:
    if reach + 30 >= i:
        count += 1
print(count)