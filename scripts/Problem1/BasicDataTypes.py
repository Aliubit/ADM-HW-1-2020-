# List Comprehensions

x = int(input())
y = int(input())
z = int(input())
n = int(input()) 

array = []

for i in range (x+1):
    for j in range(y+1):
        for k in range(z+1):
            if (i + j + k) != n:
                newArray = [i,j,k]
                array.append(newArray)

print(array)

# Find the Runner-Up Score!

n = int(input())
arr = map(int, input().split())
print(sorted(list(set(arr)))[-2])

# Nested Lists

grade_sheet = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    grade_sheet.append([name, score])

second_lowest = sorted(list(set([grades for name, grades in grade_sheet])))[1]
print('\n'.join([a for a, b in sorted(grade_sheet) if b == second_lowest]))

# Finding the percentage

n = int(input())
student_marks = {}
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores

query_name = input()
query_scores = student_marks[query_name]
avg = sum(query_scores) / 3.0
print("%.2f" % avg)

# Lists

array = []
for _ in range(int(input())):
    command = input().strip().split(" ")
    cmd_type = command[0]
    if (cmd_type == "print"):
        print(array)
    elif (cmd_type == "sort"):
        array.sort()
    elif (cmd_type == "reverse"):
        array.reverse()
    elif (cmd_type == "pop"):
        array.pop()
    elif (cmd_type == "remove"):
        array.remove(int(command[1]))
    elif (cmd_type == "append"):
        array.append(int(command[1]))
    elif (cmd_type == "insert"):
        array.insert(int(command[1]), int(command[2]))


# Tuples

input()
integer_list = map(int, input().split())
print(hash(tuple(integer_list)))
