from collections import defaultdict
graph = defaultdict(list, {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6],
    4: [2],
    5: [2],
    6: [3, 7, 8],
    7: [6],
    8: [6]
})



count = 0
leaf = None
def dfs(node,prev,depth):
    global leaf
    global count

    if depth > count:
        leaf = node
        count += 1
    
    for n in graph[node]:
        if n != prev:
            dfs(n,node,depth + 1)
    


def diameter():
    global count
    dfs(1,-1,0)

    count = 0

    dfs(leaf,-1,0)


diameter()
print(count)

