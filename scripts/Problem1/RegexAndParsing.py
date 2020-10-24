# **** Detect Floating Point Number ****

from re import match, compile

pattern = compile('^[-+]?[0-9]*\.[0-9]+$')
for _ in range(int(input())):
    print(bool(pattern.match(input())))

# **** Re.split() ****

regex_pattern = r'[.,]+'

import re
print("\n".join(re.split(regex_pattern, input())))

# **** Group(), Groups() & Groupdict() ****

import re

m = re.search(r'([a-zA-Z0-9])\1', input().strip())
print(m.group(1) if m else -1)

# **** Re.findall() & Re.finditer() ****

import re

vowels = 'aeiou'
consonants = 'qwrtypsdfghjklzxcvbnm'
match = re.findall(r'(?<=[' + consonants + '])([' + vowels + ']{2,})(?=[' + consonants + '])', input(), flags=re.I)
print('\n'.join(match or ['-1']))

# **** Re.start() & Re.end() ****

import re

string = input()
substring = input()

pattern = re.compile(substring)
match = pattern.search(string)
if not match: print('(-1, -1)')
while match:
    print('({0}, {1})'.format(match.start(), match.end() - 1))
    match = pattern.search(string, match.start() + 1)

# **** Regex Substitution ****

import re

for _ in range(int(input())):
    print(re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', input()))

# **** Validating Roman Numerals ****

regex_pattern = r'M{0,3}(C[MD]|D?C{0,3})(X[CL]|L?X{0,3})(I[VX]|V?I{0,3})$'

import re
print(str(bool(re.match(regex_pattern, input()))))

# **** Validating phone numbers ****

import re

[print('YES' if re.match(r'[789]\d{9}$', input()) else 'NO') for _ in range(int(input()))]

# **** Validating and Parsing Email Addresses ****

import re

pattern = r'^<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>$'
for _ in range(int(input())):
    name, email = input().split(' ')
    if re.match(pattern, email):
        print(name, email)

# **** Hex Color Code ****

import re

for _ in range(int(input())):
    matches = re.findall(r':?.(#[0-9a-fA-F]{6}|#[0-9a-fA-F]{3})', input())
    if matches:
        print(*matches, sep='\n')
    
# **** HTML Parser - Part 1 ****

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ('Start :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])

    def handle_endtag(self, tag):
        print ('End   :', tag)

    def handle_startendtag(self, tag, attrs):
        print ('Empty :', tag)
        for ele in attrs:
            print ('->', ele[0], '>', ele[1])


parser = MyHTMLParser()
for _ in range(int(input())):
    parser.feed(input())

# **** HTML Parser - Part 2 ****

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_comment(self, comment):
        if '\n' in comment:
            print('>>> Multi-line Comment')
        else:
            print('>>> Single-line Comment')

        print(comment)

    def handle_data(self, data):
        if data == '\n': return
        print('>>> Data')
        print(data)


html = ""
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'

parser = MyHTMLParser()
parser.feed(html)
parser.close()

# **** Detect HTML Tags, Attributes and Attribute Values ****

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


html = '\n'.join([input() for _ in range(int(input()))])
parser = MyHTMLParser()
parser.feed(html)
parser.close()

# **** Validating UID ****

import re

for _ in range(int(input())):
    u = ''.join(sorted(input()))
    try:
        assert re.search(r'[A-Z]{2}', u)
        assert re.search(r'\d\d\d', u)
        assert not re.search(r'[^a-zA-Z0-9]', u)
        assert not re.search(r'(.)\1', u)
        assert len(u) == 10
    except:
        print('Invalid')
    else:
        print('Valid')


# *** Validating Credit Card Numbers **** 

import re

pattern = re.compile(
    r'^'
    r'(?!.*(\d)(-?\1){3})'
    r'[456]\d{3}'
    r'(?:-?\d{4}){3}'
    r'$')
for _ in range(int(input().strip())):
    print('Valid' if pattern.search(input().strip()) else 'Invalid')

# **** Validating Postal Codes ****

regex_integer_in_range = r'^[1-9][\d]{5}$'  # Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r'(\d)(?=\d\1)'  # Do not delete 'r'.


import re
P = input()

print (bool(re.match(regex_integer_in_range, P)) 
and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)

# **** Matrix Script ****

import re

n, m = map(int, input().split())
a, b = [], ''
for _ in range(n):
    a.append(input())

for z in zip(*a):
    b += ''.join(z)

print(re.sub(r'(?<=\w)([^\w]+)(?=\w)', ' ', b))

