comet = input().strip()
team = input().strip()

res_comet, res_team = 1, 1
for char in comet:
    res_comet *= (ord(char) - 64)
for char in team:
    res_team *= (ord(char) - 64)

if res_comet % 47 == res_team % 47:
    print("GO")
else:
    print("STAY")