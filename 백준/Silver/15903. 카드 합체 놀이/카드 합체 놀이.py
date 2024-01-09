import heapq
import sys

n, m = map(int, sys.stdin.readline().split())
cardList = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cardList)
answer = 0

for _ in range(m):
    sumCard = heapq.heappop(cardList) + heapq.heappop(cardList)
    heapq.heappush(cardList, sumCard)
    heapq.heappush(cardList, sumCard)

for cardNum in cardList:
    answer += cardNum

print(answer)
