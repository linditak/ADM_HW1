# -*- coding: utf-8 -*-
"""
ADM_HW1

Sun Oct 25 2020
"""
# ===== PROBLEM1 =====
# Exercise 1 - Introduction - Say "Hello, World!" With Python
my_string = "Hello, World!"
print(my_string)
#
# Exercise 2 - Introduction - Python If-Else
n = int(input())
if (n >= 1 and n <= 100):
    if (n % 2 != 0 or (n >= 6 and n <= 20)):
        print("Weird")
    else:
        print("Not Weird")
#        
# Exercise 3 - Introduction - Arithmetic Operators
a = int(input())
b = int(input())
if ((a >= 1 and a <= 10**10) and (b >= 1 and b <= 10**10)):
    print(a + b)
    print(a - b)
    print(a * b)
#    
# Exercise 4 - Introduction - Python: Division
a = int(input())
b = int(input())
print(a // b)
print(a / b)
#
# Exercise 5 - Introduction - Loops
n = int(input())
if (n >= 1 and n <= 20):
    for i in range(n):
        print(i ** 2)
#        
# Exercise 6 - Introduction - Write a function
def is_leap(year):
    leap = False
    if (year in range(1900, 10**5 +1)):
        if((year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)):
            leap = True
    return leap
#
# Exercise 7 - Introduction - Print Function
n = int(input())
s = ""
for i in range(1, n +1):
    s += str(i)
print(s)
#
# Exercise 8 - Basic data types - List Comprehensions
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if(i + j + k != n)])
#
# Exercise 9 - Basic data types - Find the Runner-Up Score!
n = int(input())
arr = map(int, input().split())
s = set(arr)
if((n >=2 and n <= 10) and (min(s) >= -100 and max(s) <= 100)):
    s.remove(max(s))
    print(max(s))
#        
# Exercise 10 - Basic data types - Nested Lists
n = int(input())
if (n >= 2 and n <= 5):
    name_grade_list = []
    grade_list = []
    for _ in range(n):
        name = input()
        score = float(input())
        name_grade_list.append([name, score])
        grade_list.append(score)
    grade_set = set(grade_list)
    if (len(grade_set) > 1):
         second_lowest = sorted(list(grade_set))[1]
         for st in sorted(name_grade_list):
             if (st[1] == second_lowest):
                 print(st[0])
#                 
# Exercise 11 - Basic data types - Finding the percentage
n = int(input())
if (n >= 2 and n <= 10):
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    if (min(student_marks[query_name]) >= 0 and max(student_marks[query_name]) <= 100):
        query_mean = sum(student_marks[query_name]) / 3
        print("{:.2f}".format(query_mean))
#        
# Exercise 12 - Basic data types - Lists
n = int(input())
my_list = []
for _ in range(n):
    command, *line = input().split()
    params = list(map(int, line))
    if (command == "insert"):
        my_list.insert(params[0], params[1])
    elif (command == "print"):
        print(my_list)
    elif (command == "remove"):
        my_list.remove(params[0])
    elif (command == "append"):
        my_list.append(params[0])
    elif (command == "sort"):
        my_list.sort()
    elif (command == "pop"):
        my_list.pop()
    elif (command == "reverse"):
        my_list.reverse()
#        
# Exercise 13 - Basic data types - Tuples
n = int(input())
integer_list = list(map(int, input().split()))
t = tuple(integer_list)
print(hash(t))
#
# Exercise 14 - Strings - sWAP cASE
def swap_case(s):
    if (len(s) >= 0 and len(s) <= 1000):
        return s.swapcase()

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
#    
# Exercise 15 - Strings - String Split and Join
def split_and_join(line):
    # write your code here
    s = "-".join(line.split(" "))
    return s

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
#      
# Exercise 16 - Strings - What's Your Name?
def print_full_name(a, b):
    if (len(a) <= 10 and len(b) <= 10):
        print("Hello {} {}! You just delved into python.".format(a, b))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)
#        
# Exercise 17 - Strings - Mutations
def mutate_string(string, position, character):
    string = string[:position] + character + string[position +1:]
    return string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
#
# Exercise 18 - Strings - Find a string
def count_substring(string, sub_string):
    resp = 0
    if (len(string) >= 1 and len(string) <= 200):
        for i in range(len(string)):
            if string[i: i + len(sub_string)] == sub_string:
                resp += 1
    return str(resp)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
#
# Exercise 19 - Strings - String Validators
s = input()
if (len(s) > 0 and len(s) < 1000):
    print(any(i.isalnum() for i in s))
    print(any(i.isalpha() for i in s))
    print(any(i.isdigit() for i in s))
    print(any(i.islower() for i in s))
    print(any(i.isupper() for i in s))
#        
# Exercise 20 - Strings - Text Alignment
thickness = int(input()) #This must be an odd number
if (thickness % 2 != 0 and thickness > 0 and thickness < 50):
    c = 'H'

    #Top Cone
    for i in range(thickness):
        print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

    #Top Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

    #Middle Belt
    for i in range((thickness+1)//2):
        print((c*thickness*5).center(thickness*6))    

    #Bottom Pillars
    for i in range(thickness+1):
        print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

    #Bottom Cone
    for i in range(thickness):
        print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
        
# Exercise 21 - Strings - Text Wrap
import textwrap
def wrap(string, max_width):
    if (len(string) > 0 and len(string) < 1000 and max_width > 0 and max_width < len(string)):
        return textwrap.fill(string, max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
#    
# Exercise 22 - Strings - Designer Door Mat
nm = list(map(int, input().split()))
n = nm[0]
m = nm[1]
if (n > 5 and n < 101 and m / n == 3):
    c = ".|."
    for i in range (1, n // 2 +1):
        if i == 1:
            print(c.center(m, "-"))
        else:
            print((c *(2 * i - 1)).center(m, "-"))
    print("WELCOME".center(m, "-"))
    for i in range (n // 2 +1, n):
        print((c *(2 * (n - i) - 1)).center(m, "-"))
#        
# Exercise 23 - Strings - String Formatting
def print_formatted(number):
    # your code goes here
    if (n >= 1 and n <= 99):
        for i in range(1, n +1):
            print("{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width = len("{0:b}".format(n))))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
#            
# Exercise 24 - Strings - Alphabet Rangoli
# Exercise 25 - Strings - Capitalize!
import os
def solve(s):
    if (len(s) > 0 and len(s) < 1000 and s.replace(" ", "").isalnum()):
        return (" ".join(word.capitalize() for word in s.split(" ")))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
#
# Exercise 26 - Strings - The Minion Game
def minion_game(string):
    # your code goes here
    if (len(string) > 0 and len(string) <= 10**6):
        p1 = 0
        p2 = 0
        for i in range(len(string)):
            if string[i].upper() in "AEIOU":
                p1 += len(string) - i
            else:
                p2 += len(string) - i
        if (p1 > p2):
            print("Kevin " + str(p1))
        elif (p1 < p2):
            print("Stuart " + str(p2))
        else:
            print("Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)
#
# Exercise 27 - Strings - Merge the Tools!
def merge_the_tools(string, k):
    # your code goes here
    if (len(string) in range(1, 10**4 + 1) and k in range(1, len(string) + 1)):
        parts = [string[i:i+k] for i in range(0, len(string), k)]
        for j in range(len(parts)):
            n_string = parts[j][0]
            for c in parts[j][1:]:
                if c not in n_string:
                    n_string += c
            print(n_string)
  

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
#
# Exercise 28 - Sets - Introduction to Sets
def average(array):
    # your code goes here
    if (n > 0 and n <= 100):
        s = set(array)
        return (sum(s) / len(s))
#
# Exercise 29 - Sets - No Idea!
happiness = 0
n, m = map(int, input().split())
if ((n >= 1  and n <= 10 ** 5) and (m >= 1  and m <= 10 ** 5)):
    arr = list(map(int, input().split()))
    if (min(arr) >= 1 and max(arr) < 10 ** 9):
        set_a = set(list(map(int, input().split())))
        if (min(set_a) >= 1 and max(set_a) < 10 ** 9):
            set_b = set(list(map(int, input().split())))
            if (min(set_b) >= 1 and max(set_b) < 10 ** 9):
                for i in range(len(arr)):
                    if (arr[i] in set_a):
                        happiness += 1
                    elif (arr[i] in set_b):
                        happiness -= 1
                print(happiness)
#
# Exercise 30 - Sets - Symmetric Difference
m = int(input())
l_m = list(map(int, input().split()))
n = int(input())
l_n = list(map(int, input().split()))
l_diff = list((set(l_m) ^ set(l_n)))
l_diff.sort()
for x in l_diff:
    print(x)
#
# Exercise 31 - Sets - Set .add()
n = int(input())
if (n > 0 and n < 1000):
    s_countries = set()
    for i in range(n):
        country = input()
        s_countries.add(country)
    print(len(s_countries))
#
# Exercise 32 - Sets - Set .discard(), .remove() & .pop()
n = int(input())
if (n > 0 and n < 20):
    s = set(map(int, input().split()))
    n_commands = int(input())
    if (n_commands > 0 and n_commands < 20):
        for _ in range(n_commands):
            command, *line = input().split()
            params = list(map(int, line))
            if (command == "pop"):
                s.pop()
            elif(command == "remove"):
                s.remove(params[0])
            elif(command == "discard"):
                s.discard(params[0])
        print(sum(s))
#
# Exercise 33 - Sets - Set .union() Operation
eng_n = int(input())
if(eng_n > 0 and eng_n < 1000):
    eng_std = list(map(int, input().split()))
    fr_n = int(input())
    if (fr_n > 0 and fr_n < 1000):
        fr_std = list(map(int, input().split()))
        length = len(set(eng_std).union(set(fr_std)))
        if(length > 0 and length < 1000):
            print(length)
#
# Exercise 34 - Sets - Set .intersection() Operation
eng_n = int(input())
if(eng_n > 0 and eng_n < 1000):
    eng_std = list(map(int, input().split()))
    fr_n = int(input())
    if (fr_n > 0 and fr_n < 1000):
        fr_std = list(map(int, input().split()))
        length = len(set(eng_std).intersection(set(fr_std)))
        if(length > 0 and length < 1000):
            print(length)
#
# Exercise 35 - Sets - Set .difference() Operation
eng_n = int(input())
if(eng_n > 0 and eng_n < 1000):
    eng_std = list(map(int, input().split()))
    fr_n = int(input())
    if (fr_n > 0 and fr_n < 1000):
        fr_std = list(map(int, input().split()))
        length = len(set(eng_std).difference(set(fr_std)))
        if(length > 0 and length < 1000):
            print(length)
#
# Exercise 36 - Sets - Set .symmetric_difference() Operation
eng_n = int(input())
if(eng_n > 0 and eng_n < 1000):
    eng_std = list(map(int, input().split()))
    fr_n = int(input())
    if (fr_n > 0 and fr_n < 1000):
        fr_std = list(map(int, input().split()))
        length = len(set(eng_std).symmetric_difference(set(fr_std)))
        if(length > 0 and length < 1000):
            print(length)
#
# Exercise 37 - Sets - Set Mutations
n_a = float(input())
if (n_a > 0 and n_a < 1000):
    set_a = set(list(map(float, input().split())))
    len_a = len(set_a)
    if(len_a > 0 and len_a < 1000):
        n_other = int(input())
        for _ in range(n_other):
            command, s_len_other = input().split()
            len_other = int(s_len_other)
            if (len_other > 0 and len_other < 100):
                list_other = list(map(int, input().split()))
                set_other = set(list_other)
                if (command == "intersection_update"):
                    set_a.intersection_update(set_other)
                elif (command == "update"):
                    set_a.update(set_other)
                elif (command == "symmetric_difference_update"):
                    set_a.symmetric_difference_update(set_other)
                elif (command == "difference_update"):
                    set_a.difference_update(set_other)
        print(sum(set_a))
#
# Exercise 38 - Sets - The Captain's Room
k = int(input())
if(k > 0 and k < 1000):
    rooms = sorted(list(map(int, input().split())))
    rooms_set = set(rooms)
    family_set = set()
    for i in range(len(rooms) -1):
        if (rooms[i] == rooms[i+1]):
            family_set.add(rooms[i])
    rooms_set.difference_update(family_set)
    print(max(rooms_set))
#
# Exercise 39 - Sets - Check Subset
t = int(input())
if (t > 0 and t < 21):
    for i in range(t):
        len_a = int(input())
        if (len_a > 0 and len_a < 1001):
            set_a = set(list(map(int, input().split())))
            len_b = int(input())
            if (len_b > 0 and len_b < 1001):
                set_b = set(list(map(int, input().split())))
                print(set_a.issubset(set_b))
#           
# Exercise 40 - Sets - Check Strict Superset
set_a = set(list(map(int, input().split())))
is_super = True
if (len(set_a) > 0 and len(set_a) < 501):
    n_other = int(input())
    if(n_other > 0 and n_other < 21):
        for i in range(n_other):
            set_o = set(list(map(int, input().split())))
            is_super = is_super and set_a.issuperset(set_o)
print(is_super)
#                
# Exercise 41 - Collections - collections.Counter()
from collections import Counter
money = 0
x = int(input())
if(x > 0 and x < 10 ** 3):
    all_sizes = list(map(int, input().split()))
    capacity = Counter(all_sizes)
    n = int(input())
    if(n > 0 and n <= 10 ** 3):
        for i in range(n):
            customer_size, price = map(int, input().split())
            if (customer_size in range(2, 21) and price in range(20, 101)):
                if(capacity[customer_size] > 0):
                    money = money + price
                    capacity[customer_size] -= 1
        print(money)
#
# Exercise 42 - Collections - DefaultDict Tutorial
from collections import defaultdict
next_step = True
n, m = map(int, input().split())
if(n in range(1,10001) and m in range(1,101)):
    d_a = defaultdict(list)
    for i in range(n):
        w_a = input()
        if (len(w_a) in range(1, 101)):
            d_a[i] = (w_a)
        else:
            next_step = False
            break
    if next_step:
        for j in range(m):
            w_b = input()
            if (len(w_b) in range(1, 101)):
                output = ""
                keys = [key for (key, value) in d_a.items() if value == w_b]
                if (len(keys) > 0):
                    for key in keys:
                        output = output + str(key +1) + " "
                else:
                    output = "-1"
                print(output)
#
# Exercise 43 - Collections - Collections.namedtuple()
from collections import namedtuple
n = int(input())
if (n in range(101)):
    Student = namedtuple("Student", input())
    st = [(Student._make(input().split())) for i in range(n)]
    print("{:.2f}".format(sum(int(Student.MARKS) for Student in st)/n))
#
# Exercise 44 - Collections - Collections.OrderedDict()
from collections import OrderedDict
from collections import Counter
n = int(input())
if n in range(101):
    l = []
    d = OrderedDict()
    for _ in range (n):
        k,v = input().rsplit(" ", 1)
        l.append(k)
        d[k] = v
    c= Counter(l)
    for e in d.items():
        net_price = int(e[1])*int(c[e[0]])
        print(" ".join([e[0], str(net_price)]))
#
# Exercise 45 - Collections - Word order
from collections import Counter
n = int(input())
if n in range(1, 10**5+1):
    words = []
    w_len=0
    for _ in range(n):
        x = input()
        words.append(x)
        w_len += len(x)
    if w_len in range(1, 10**6 +1):
        s_words = Counter(words)
        l_words = []
        for w in s_words.values():
            l_words.append(str(w))
        print(len(l_words))
        print(" ".join(l for l in l_words))
#
# Exercise 46 - Collections - Collections.deque()
from collections import deque
n = int(input())
if n in range (1, 101):
    d = deque()
    for _ in range(n):
        command, *line = input().split()
        params = list(map(int, line))
        if (command == "append"):
            d.append(params[0])
        elif (command == "appendleft"):
            d.appendleft(params[0])
        elif (command == "pop"):
            d.pop()
        elif (command == "popleft"):
            d.popleft()
    print(" ".join(str(s) for s in d))
#
# Exercise 47 - Collections - Company Logo
from collections import Counter
if __name__ == '__main__':
    s = input()
    if (len(s) in range (3, 10**4 +1)):
        c = Counter(s)
        cm = c.most_common()
        cm.sort(key = lambda x:(-x[1], x[0]))
        for i in range(3):
            print(" ".join(map(str, cm[i])))
#
# Exercise 48 - Collections - Piling Up
#
# Exercise 49 - Date and Time - Calendar Module
import datetime
m,d,y = list(map(int, input().split()))
if y in range(2000, 3000+1):
    print(datetime.date(y, m, d).strftime('%A').upper())
#