import sys
from io import StringIO


input_string = """4
35
54
80
12"""


sys.stdin = StringIO(input_string)

max_rup = 100
for _ in range(int(input())):
    cost = int(input())

    if cost % 10 == 0:
        print(max_rup - cost)
        continue
    

    last_dig = cost % 10
    if last_dig >= 5:
        res = cost + (10 - last_dig)

    else:
        res = cost - last_dig

    print(max_rup - res)
