import sys
budget = list(int(input().strip()) for _ in range(12))

money, deposit = 0, 0
for i in range(12):
    money += 300
    money -= budget[i]
    if money // 100 > 0:
        deposit += ((money // 100) * 100)
        money %= 100
    if money < 0:
        print(-(i + 1))
        sys.exit()
print(int(money + deposit * 1.2))