import sys

n = int(input())
timeList = list(map(int, sys.stdin.readline().split()))
timeList.sort()
result = list()
count = 0

for i in timeList:
    count += i
    result.append(count)

print(sum(result))
