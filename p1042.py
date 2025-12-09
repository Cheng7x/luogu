import sys
data = sys.stdin.read().splitlines()
def simulate(target):
    p1, p2 = 0, 0
    score = []
    for line in data:
        for c in line:
            if c == 'W':
                p1 += 1
            elif c == 'L':
                p2 += 1
            elif c == 'E':
                return score, p1, p2

            if (abs(p1 - p2) >= 2) and (max(p1, p2) >= target):
                score.append((p1, p2))
                p1, p2 = 0, 0
                
def print_score(score, p1, p2):
    for _, (player1, player2) in enumerate(score):
        print(f"{player1}:{player2}")
    print(f"{p1}:{p2}")

print_score(*simulate(11))
print()
print_score(*simulate(21))
