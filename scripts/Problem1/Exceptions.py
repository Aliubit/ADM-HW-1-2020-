# **** Exceptions **** 

for _ in range(int(input())):
    a, b = input().split()
    try:
        print(int(a) // int(b))
    except Exception as e:
        print('Error Code: ' + str(e))


# **** Incorrect Regex ****

import re

for _ in range(int(input())):
    try:
        re.compile(input())
        print(True)
    except Exception as e:
        print(False)

