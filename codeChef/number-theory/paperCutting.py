"""
--------------------- PAPER CUTTING --------------------
we will be givin a square with its length and another length as input.
we need to dettermine how many sqaure can be made from the main square we have
based on input we get.

we get N as Square length and K as length we want to derive sqaure based on K.

0 < K <= N

Exp: we have 5x5 length square how many square of 2x2 can be dervied.

answer = 5 / 2 * 5 / 2 => 2.5 * 2.5 => 2 * 2 = 4 ->>> we must round down the
division answer.

we can have 4 sqaure of 2x2 from 5x5 sqaure.
"""

import sys
from io import StringIO
import math

input_string = """3
5 1
2 2
5 2"""

sys.stdin = StringIO(input_string)

for _ in range(int(input())):
    n, k = list(map(int, input().split()))

    ans = math.floor(n / k) * math.floor(n / k)

    print(ans)
