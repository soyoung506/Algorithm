import heapq
import sys

n = int(input())
heapList = []

for _ in range(n):
    num = int(sys.stdin.readline())

    if num == 0:
        if heapList:
            print(heapq.heappop(heapList)[1])
        else:
            print(0)
    else:
        heapq.heappush(heapList, (-num, num))
