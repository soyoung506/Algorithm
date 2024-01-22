import heapq
import sys

n = int(input())
timeList = list(map(int, sys.stdin.readline().split()))
result = list()
count = 0

for i in range(1, n + 1):
    count += heapq.nsmallest(i, timeList)[-1]
    result.append(count)

print(sum(result))
