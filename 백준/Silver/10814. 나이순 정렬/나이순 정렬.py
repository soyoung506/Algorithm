import sys

n = int(input())
ageList = []

for _ in range(n):
    age, name = sys.stdin.readline().split()
    ageList.append([int(age), name])

ageList.sort(key=lambda x: x[0])

for age, name in ageList:
    print(age, name)
