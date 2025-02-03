"""
----------------------------- Supporting Everyone ---------------------

We have to support all countries by buying either cryans of thier flag or,
buying a pin which is the country name.

each cryan cost  -----> 1
each pin cost ------> 1

Input:
7 6 -------> 7 are country numbers, 6 is colors
3 -----> next line has 3 color
1 4 5 -----> we can buy each one or buy a pin for whole flag
3
1 4 5
3
1 4 5
3
3 4 5
3
3 4 5
3
3 4 5
3
2 5 6


Explain:
colors are: 1 2 3 4 5 6

Output:
5


we have to find the miniuim cost to support all countries.
"""

import sys
from io import StringIO
from collections import defaultdict
from typing import Tuple

"""--------------------- TEST CASES ------------------------"""
input_string = """7 6
3
1 4 5
3
1 4 5
3
1 4 5
3
3 4 5
3
3 4 5
3
3 4 5
3
2 5 6"""


input_string2 = """8 12
2
7 9
12
1 2 3 4 5 6 7 8 9 10 11 12
2
7 9
2
7 9
3
3 4 11
2
7 9
2
7 9
2
7 9"""


input_string3 = """3 4
2
1 2
2
2 3
2
3 4"""

input_string4 = """4 6
3
1 2 3
3
3 4 5
3
2 3 6
6
1 2 3 4 5 6"""


input_string5 = """5 7
3
1 2 3
3
3 4 5
3
5 6 7
1
7
3
1 4 7"""
"""------------------------------ Code -----------------------------"""

sys.stdin = StringIO(input_string5)

co, cl = list(map(int, input().split()))

items = defaultdict(int)
min_cost = 0


buyed_colors = []


def shouldBuy(colors: Tuple):
    cost = 0
    for c in colors:
        if c not in buyed_colors:
            buyed_colors.append(c)
            cost += 1
    return cost


for _ in range(co):
    num_color = int(input())
    colors = tuple(map(int, input().split()))
    items[colors] += 1


for key, val in items.items():
    print(key)
    print(val)
    if val > 1:
        cost = shouldBuy(key)
        min_cost += cost

    if val == 1:
        min_cost += 1

print(min_cost)
