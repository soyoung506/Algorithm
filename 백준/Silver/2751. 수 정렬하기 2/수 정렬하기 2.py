n = int(input())
numList = []

for _ in range(n):
    num = int(input())
    numList.append(num)

numList.sort()

for num in numList:
    print(num)
    