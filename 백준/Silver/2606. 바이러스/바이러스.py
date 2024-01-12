n = int(input())
d = int(input())
visited = [False] * (n+1)

edges = [map(int, input().split()) for _ in range(d)]
graph = [[] for _ in range(n+1)]


for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
stack = [1]
visited[1] = True

while stack:
    node = stack.pop()

    # 연결된 노드들에 대해서 방문한 적이 없는 노드들만 탐색
    for nxt in graph[node]:
        if visited[nxt]:
            continue

        cnt += 1
        visited[nxt] = True
        stack.append(nxt)


print(cnt)