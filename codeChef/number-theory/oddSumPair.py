"""
------------------------- ODD Sum pair --------------------------
the problem is easy we will be given a 3 integer and among those integer we should check this:
if their are 2 numbers which sum of them is an odd we print (Yes) otherwise (No)

isn't that simple!!!



just check if there are any number that is even and also a odd number among 3 numbers.

cause odd + even = odd -> REMEMBER this Number THEORY Boy!!!
"""


import sys
from io import StringIO


input_string = """4
1 2 3
8 4 6
3 3 9
7 8 6"""


sys.stdin = StringIO(input_string)


for _ in range(int(input())):
    odd_check = False
    even_check = False
    
    
    nums = list(map(int, input().split()))
    for i in nums:
        if i % 2 == 0:
            even_check = True
        
        if i % 2 != 0:
            odd_check = True
    
    if even_check and odd_check:
        print("yes")
    
    else:
        print("no")
