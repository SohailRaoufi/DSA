"""
Online or Offline

Chef is confused whether to go out and eat at the restaurant or order food online.

The online order costs NN rupees while the cost of eating at the restaurant is MM rupees.
However, Chef has a discount coupon with which he can avail flat 10%10% off on his online order.

Find the cheaper option for Chef to eat, i.e., whether to order food online or eat at the restaurant.
N -> Online
M -> Dining

output:
N = M -> Either
N > M -> Dining
N < M -> Online
"""

import sys
from io import StringIO

input_string = """4
500 500
500 400
25 22
100 90"""

sys.stdin = StringIO(input_string)


discount = 90
for _ in range(int(input())):
    n, m = list(map(int, input().split()))

    dis_n = (n * discount) / 100

    if dis_n > m:
        res = "Dining"
    elif dis_n < m:
        res = "Online"
    else:
        res = "Either"


    print(res)
