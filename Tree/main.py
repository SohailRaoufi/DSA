from collections import defaultdict
adj = defaultdict(list)

data = [
    (1,2), (1,3), (2,4), (2,5), (4,6),
]

for u,v in data:
    adj[u].append(v)

count = {}

def dfs(node,prev):
    count[node] = 1
    arr = adj[node]
    for n in arr:
        if(n == prev): continue
        dfs(n,node)
        count[node] += count[n]


dfs(2,1)
print(count[2])