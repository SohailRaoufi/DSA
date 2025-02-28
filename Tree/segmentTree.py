from typing import List

arr = [1, 3, 5, 7, 9, 11]

segment_tree = [0] * (4 * len(arr))


def build(arr: List, v, tl, tr):
    if tl == tr:
        segment_tree[v] = arr[tl]
    else:
        tm = (tl + tr) // 2
        build(arr, v * 2 + 1, tl, tm)
        build(arr, v * 2 + 2, tm + 1, tr)
        segment_tree[v] = segment_tree[v * 2 + 1] + segment_tree[v * 2 + 2]



def sum(v, tl, tr, l, r):
    if(l > r):
        return 0
    if(tl == l and tr == r):
        return segment_tree[v]
    tm = (tr + tl) // 2
    return sum(v * 2+1, tl, tm, l, min(r, tm)) + sum(v*2+2, tm+1, tr, max(l, tm + 1), r)


build(arr, 0, 0, len(arr) - 1)


res = sum(0, 0, len(arr) - 1, 0, len(arr) - 1)
print(res)
print(segment_tree)
