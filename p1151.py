k = int(input().strip())

flag = False
for i in range(10000, 30001):
    i = str(i)
    sub1 = int(i[0:3])
    sub2 = int(i[1:4])
    sub3 = int(i[2:5])

    if sub1 % k == sub2 % k == sub3 % k == 0:
        print(i)
        flag = True

if flag == False:
    print("No")