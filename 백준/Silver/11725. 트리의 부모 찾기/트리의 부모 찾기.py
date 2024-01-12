from sys import stdin
def input(): return stdin.readline().rstrip()


n = int(input())
edges = [map(int, input().split()) for _ in range(n-1)]

graph = [[] for _ in range(n+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)


root = 1
parents = [0] * (n+1)
parents[root] = -1


stack = [root]
while stack:
    node = stack.pop()
    for child in graph[node]:
        if parents[child] != 0:
            continue
        parents[child] = node
        stack.append(child)

print(*parents[2:], sep='\n')