"""
exp = [1] , [], [1, 2] =>           1,    ,     1
                                               / \
                                              1   2 -> min(1, 2) = 1

t = [0, 0, 0, 0] => [1, 1, 2, 0]
"""

arr = [1, 2, 5, 7, 9, 3]

a = [1, 2]

t = [0] * (2 * len(a))


def min_build(v, start, end):
    if start == end:
        t[v] = a[start]
        return

    tm = (start + end) // 2

    min_build(v * 2, start, tm)
    min_build(v * 2 + 1, tm + 1, end)

    t[v] = min(t[v * 2], t[v * 2 + 1])


min_build(1, 0, len(a) - 1)

print(t)
