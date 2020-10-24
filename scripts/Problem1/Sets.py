# **** Introduction to Sets ****

def average(array):
    distinct_heights = set(array)
    return sum(distinct_heights) / len(distinct_heights)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# **** No Idea! *****

n, m = input().split()

array = input().split()
A = set(input().split())
B = set(input().split())

print(sum([(i in A) - (i in B) for i in array]))


# **** Symmetric Difference *****

m = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))

print(*sorted(a.symmetric_difference(b)), sep='\n')

# **** Set .add() ****

stamps = set()
for _ in range(int(input())):
    stamps.add(input())
print(len(stamps))

# ***** Set .discard(), .remove() & .pop() ****

n = input()
elements = set(map(int, input().split()))

for _ in range(int(input())):
    command = input().split()
    operation = command[0]
    args = command[1:]

    if operation != 'pop':
        operation += '(' + ','.join(args) + ')'
        eval('elements.' + operation)
    else:
        elements.pop()
print(sum(elements))

# **** Set .union() Operation ****

_, en_subscribers = input(), set(map(int, input().split())) 
_, fr_subscribers = input(), set(map(int, input().split())) 
print(len(en_subscribers.union(fr_subscribers)))

# **** Set .intersection() Operation ****

_, en_subscribers = input(), set(map(int, input().split())) 
_, fr_subscribers = input(), set(map(int, input().split())) 
print(len(en_subscribers.intersection(fr_subscribers)))

# **** Set .difference() Operation ****

_, en_subscribers = input(), set(map(int, input().split())) 
_, fr_subscribers = input(), set(map(int, input().split())) 
print(len(en_subscribers.difference(fr_subscribers)))

# **** Set .symmetric_difference() Operation ****

_, en_subscribers = input(), set(map(int, input().split())) 
_, fr_subscribers = input(), set(map(int, input().split())) 
print(len(en_subscribers.symmetric_difference(fr_subscribers)))

# **** Set Mutations ****

N = input()
A = set(map(int, input().split())) 

for _ in range(int(input())):
    command = input().split()[0]
    elements = input().split()
    command += '([' + ','.join(elements) + '])'
    eval('A.' + command)
print(sum(A))

# **** The Captain's Room ****

K = int(input())

room_list = list(map(int, input().split()))
room_set = set(room_list)
sum_room_list = sum(room_list)
sum_room_set = sum(room_set)
diff = sum_room_set * K - sum_room_list

print(diff // (K - 1))

# **** Check Subset ****

for _ in range(int(input())):
    a, A = input(), set(input().split())
    b, B = input(), set(input().split())

    print(A.issubset(B))

# **** Check Strict Superset ****

A = set(input().split())

for _ in range(int(input())):
    if not A.issuperset(set(input().split())):
        print(False)
        break
else:
    print(True)

