# **** collections.Counter() *****

from collections import Counter

num_shoes = int(input())
shoe_sizes = Counter(map(int, input().split()))
num_customers = int(input())

cost = 0
for _ in range(num_customers):
    size, price = map(int, input().split())
    if shoe_sizes[size]:
        cost += price
        shoe_sizes[size] -= 1

print(cost)

# **** DefaultDict Tutorial ****

from collections import defaultdict

d = defaultdict(list)
n, m = map(int, input().split())

for i in range(n):
    d[input()].append(str(i + 1))
for j in range(m):
    print(' '.join(d[input()]) or -1)

# **** Collections.namedtuple() ****

from collections import namedtuple

n = int(input())
fields = input().split()

total_marks = 0
for _ in range(n):
    students = namedtuple('student', fields)
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    total_marks += int(student.MARKS)
print('{:.2f}'.format(total_marks / n))

# **** Collections.OrderedDict() ****

from collections import OrderedDict

order = OrderedDict()
for _ in range(int(input())):
    item, space, price = input().rpartition(' ')
    order[item] = order.get(item, 0) + int(price)
for item, price in order.items():
    print(item, price)

# **** Word Order ****

from collections import OrderedDict

dict = OrderedDict()

for _ in range(int(input())):
    key = input()
    dict[key] = dict.get(key, 0) + 1

print(len(dict))
print(*dict.values())

# **** Collections.deque() *****

from collections import deque

d = deque()
for i in range(int(input())):
    command = input().split()
    if command[0] == 'append':
        d.append(command[1])
    elif command[0] == 'appendleft':
        d.appendleft(command[1])
    elif command[0] == 'pop':
        d.pop()
    else:
        d.popleft()
print(' '.join(d))

# **** Company Logo ****

import collections

s = sorted(input().strip())
s_counter = collections.Counter(s).most_common()

s_counter = sorted(s_counter, key=lambda x: (x[1] * -1, x[0]))
for i in range(0, 3):
    print(s_counter[i][0], s_counter[i][1])

# **** Piling Up! ****

for t in range(int(input())):
    l = int(input())
    sides = list(map(int, input().split()))
    i = 0
    while i < l - 1 and sides[i] >= sides[i + 1]:
        i += 1
    while i < l - 1 and sides[i] <= sides[i + 1]:
        i += 1
    print('Yes' if i == l - 1 else 'No')