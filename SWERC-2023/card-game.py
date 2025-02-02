"""
--------------------------- CARD GAME IDEA ------------------------------------
Cards -------    ------------------- Priority of Cards
    S -> Silver:                            1
    W -> White:                             2
    E -> Emerlad:                           3
    R -> Red:                               4
    C -> Cyan:                              5


we have N cards in our hand and we need to organize those cards based on their
priority the higher the number the higher the prioriy. at the end we must
return minimuim number of actions taken in order
to organize the cards.

Input:
4 -> Number of Cards
C1 R2 E4 R1  -> Cards

the number in each show how much the appear and the cards could appear multiple
times.


Output:
2 -> moves taken to organize the cards based on priority.

"""

import sys
from io import StringIO

cards = {
    "C": 5,
    "R": 4,
    "E": 3,
    "W": 2,
    "S": 1
}


input_string = """4
C1 R2 E4 R1"""

input2 = """5
S2 W4 E1 R5 C1"""


def convertToCard(card):
    return cards[card[0]]


sys.stdin = StringIO(input_string)


p = input()
c = list(map(convertToCard, input().split()))

sorted_nums = 0

for i in range(len(c)):
    if c[i] == i + 1:
        sorted_nums += 1

print(len(c) - sorted_nums)
