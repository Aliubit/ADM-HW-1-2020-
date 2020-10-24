#  Hello world

print("Hello, World!")


# Python If-Else

n = int(input().strip())

if n % 2 != 0 :
    print("Weird")
else:
    # number is even
    if n >=2 and n < 6 :
        print("Not Weird")
    elif n >= 6 and n <= 20 :
        print("Weird")
    elif n > 20 :
        print("Not Weird")


# Arithmetic Operators

firstNumber = int(input())
secondNumber = int(input())

print(firstNumber + secondNumber)
print(firstNumber - secondNumber)
print(firstNumber * secondNumber)

# Python: Division


a = int(input())
b = int(input())

print(a//b)
print(a/b)

# Loops

n = int(input())
for i in range(n):
    print(i ** 2)

# Write a function

def is_leap(year):
    leap = False
    
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
        else:
            leap = True
    
    return leap

year = int(input())
print(is_leap(year))

# Print Function

n = int(input())
for i in range(1,n+1):
    print(i, end ="")