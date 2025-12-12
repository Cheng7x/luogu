n, k = map(int, input().split())
total = n  # 总共能吸的烟数
stubs = n  # 当前烟蒂数

while stubs >= k:
    new_smokes = stubs // k
    total += new_smokes
    stubs = stubs % k + new_smokes  # 剩余烟蒂 + 新烟产生的烟蒂

print(total)
