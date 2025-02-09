"""
------------------ IFTAR ----------------------
we have C people or contestents and P food each C eat Q amount P and there will be L amount P left.
find how many C ate P.

we will be given P and L.

the formula is easy we find all divisors of P-L cause the real formula is = Q * C = P - L
"""

import sys
from io import StringIO
import math

input_string = """4
10 0
13 2
300 98
1000 997"""

sys.stdin = StringIO(input_string)


def divisors_greater_than(num, l):
    res = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            if i > l:
                res.append(i)
            if (num // i) != i and (num // i) > l:
                res.append(num // i)
    return sorted(res)


t = int(input())
for case_num in range(1, t + 1):
    p, l = map(int, input().split())
    e = p - l
    result = divisors_greater_than(e, l)

    if not result:
        print(f"Case {case_num}: impossible")
    else:
        print(f"Case {case_num}: {' '.join(map(str, result))}")
