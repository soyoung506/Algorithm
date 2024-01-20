import sys


class DisjointSet:

    def __init__(self, n):
        self.parent = list(range(n + 1))

    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.parent[root_x] = root_y


n = int(input())
edgeN = int(input())
edges = []

for _ in range(edgeN):
    edge = list(map(int, sys.stdin.readline().split()))
    edges.append(edge)

edges.sort(key=lambda x: x[2])
disjoint_set = DisjointSet(n)
result = 0
used_edges = 0

for idx, adj, cost in edges:
    if idx == adj:
        continue

    if disjoint_set.find(idx) != disjoint_set.find(adj):
        disjoint_set.union(idx, adj)
        result += cost
        used_edges += 1

        if used_edges == n - 1:
            break

print(result)
