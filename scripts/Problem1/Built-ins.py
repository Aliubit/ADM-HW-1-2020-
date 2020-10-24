# **** Zipped! ****

n, x = map(int, input().split())

sheet = []
for _ in range(x):
    sheet.append(map(float, input().split()))

for i in zip(*sheet):
    print(sum(i) / len(i))

# **** Athlete Sort ****

n, m = map(int, input().split())
rows = [input() for _ in range(n)]
k = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[k])):
    print(row)

# **** ginortS ****

print(*sorted(input(), key=lambda c: (c.isdigit() - c.islower(), c in '02468', c)), sep='')