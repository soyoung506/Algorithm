import collections
import sys

# 노드수, 간선수, 시작점
nodes, edges, root = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
dfs_answer = []
bfs_answer = []
dfs_visited = [root]
bfs_visited = [root]
bfs_queue = collections.deque([root])

for _ in range(edges):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드 key의 value값들을 오름차순으로 정렬
for vals in graph.values():
    vals.sort()


def dfs(node):
    dfs_answer.append(node)

    for nxt in graph[node]:
        if nxt in dfs_visited:
            continue
        dfs_visited.append(nxt)
        dfs(nxt)


dfs(root)

while bfs_queue:
    now = bfs_queue.popleft()
    bfs_answer.append(now)

    for nxt in graph[now]:
        if nxt in bfs_visited:
            continue

        bfs_visited.append(nxt)
        bfs_queue.append(nxt)

print(*dfs_answer, sep=' ', end='\n')
print(*bfs_answer, sep=' ')