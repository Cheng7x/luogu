n, m = map(int, input().split())

votes = list(map(int, input().split()))
votes.sort()

print(''.join(map(str, votes)))