n = int(input())
d = int(input())

edges = [map(int, input().split()) for _ in range(d)]
graph = [[] for _ in range(n+1)]


for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

stack = [1]
visited = [1]

while stack:
    node = stack.pop()

    for nxt in graph[node]:
        if nxt in visited:
            continue

        visited.append(nxt)
        stack.append(nxt)


print(len(visited)-1)