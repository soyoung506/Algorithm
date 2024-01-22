import sys

t = int(input())
tList = list()
result = list()

for _ in range(t):
    recruitList = list()
    n = int(input())
    for _ in range(n):
        document, interview = map(int, sys.stdin.readline().split())
        recruitList.append((document, interview))

    recruitList.sort()
    tList.append(recruitList)

for testCase in tList:
    count = 0
    minimum = 0
    for applicant in testCase:
        if applicant[0] == 1:
            minimum = applicant[1]
            count += 1
            continue

        if minimum > applicant[1]:
            minimum = applicant[1]
            count += 1

        if minimum == 1:
            result.append(count)
            break

for case in result:
    print(case)
    