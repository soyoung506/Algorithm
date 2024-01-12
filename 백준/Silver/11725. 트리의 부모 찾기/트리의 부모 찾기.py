import collections
import sys

n = int(input())
graph = collections.defaultdict(list)
answer = [0] * (n + 1)
answer[1] = -1
stack = [1]

for _ in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

while stack:
    node = stack.pop()
    for child in graph[node]:
        if answer[child] == 0:
            answer[child] = node
            stack.append(child)

print(*answer[2:], sep='\n')
