import sys


n = int(input())
parentList = list(map(int, sys.stdin.readline().split()))
removeNode = int(input())
graph = [[] for _ in range(n)]
root = 0
stack = []
visited = [False] * n
count = 0

for idx, parent in enumerate(parentList):
    if parent == -1:
        root = idx
        continue
    graph[parent].append(idx)

if root != removeNode:
    stack.append(root)
    visited[root] = True
    graph[parentList[removeNode]].remove(removeNode)

while stack:
    node = stack.pop()

    for child in graph[node]:
        if visited[child]:
            continue
        visited[child] = True
        stack.append(child)

    if not graph[node]:
        count += 1

print(count)
