# sWAP cASE

def swap_case(s):
    return s.swapcase()


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

# String Split and Join

def split_and_join(line):
    return "-".join(line.split(" "))


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

# What's Your Name?

def print_full_name(first_name, last_name):
    print("Hello " + first_name + " " + last_name + "! You just delved into python.")


if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)

# Mutations

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

# Find a string


import re


def count_substring(string, sub_string):
    match = re.findall('(?=' + sub_string + ')', string)
    return len(match)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)

# String Validators

if __name__ == '__main__':
    str = input()
    print(any(c.isalnum() for c in str))
    print(any(c.isalpha() for c in str))
    print(any(c.isdigit() for c in str))
    print(any(c.islower() for c in str))
    print(any(c.isupper() for c in str))

# Text Alignment

#Replace all ______ with rjust, ljust or center. 

thickness = int(input())  # This must be an odd number
c = 'H'

    # Top Cone
for i in range(thickness):
    print((c * i).rjust(thickness - 1) + c + (c * i).ljust(thickness - 1))

    # Top Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Middle Belt
for i in range((thickness + 1) // 2):
    print((c * thickness * 5).center(thickness * 6))

    # Bottom Pillars
for i in range(thickness + 1):
    print((c * thickness).center(thickness * 2) + (c * thickness).center(thickness * 6))

    # Bottom Cone
for i in range(thickness):
    print(((c * (thickness - i - 1)).rjust(thickness) + c + (c * (thickness - i - 1)).ljust(thickness)).rjust(thickness * 6))

# Text Wrap

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)

# Designer Door Mat

# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = map(int, input().split())
pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1]))

# String Formatting

def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for i in range(1, number + 1):
        print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i,       width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

# Alphabet Rangoli

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    for i in range(n - 1, 0, -1):
        row = ["-"] * (n * 2 - 1)
        for j in range(0, n - i):
            row[n - 1 - j] = alpha[j + i]
            row[n - 1 + j] = alpha[j + i]
        print("-".join(row))

    for i in range(0, n):
        row = ["-"] * (n * 2 - 1)
        for j in range(0, n - i):
            row[n - 1 - j] = alpha[j + i]
            row[n - 1 + j] = alpha[j + i]
        print("-".join(row))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

# Capitalize!

import math
import os
import random
import re
import sys
    
def solve(s):
    full_name = s.split(' ')
    return ' '.join((word.capitalize() for word in full_name))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()

# The Minion Game

def minion_game(string):
    vowels = 'AEIOU'
    str_lenght = len(string)
    kevin_score, stuart_score = 0, 0

    for i in range(str_lenght):
        if s[i] in vowels:
            kevin_score += (str_lenght - i)
        else:
            stuart_score += (str_lenght - i)

    if kevin_score > stuart_score:
        print("Kevin", kevin_score)
    elif kevin_score < stuart_score:
        print("Stuart", stuart_score)
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)

# Merge the Tools!

from collections import OrderedDict


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        print(''.join(OrderedDict.fromkeys(string[i:i + k])))


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)



