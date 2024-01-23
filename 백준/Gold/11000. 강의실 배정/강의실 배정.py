import heapq
import sys

n = int(input())
timeSheet = list()
heap = []

for _ in range(n):
    s, t = map(int, sys.stdin.readline().split())
    timeSheet.append((s, t))

timeSheet.sort()

for start, end in timeSheet:
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    heapq.heappush(heap, end)

print(len(heap))
