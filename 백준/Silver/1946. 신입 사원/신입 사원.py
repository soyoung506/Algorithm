import sys

t = int(input())

for _ in range(t):
    n = int(input())
    recruitList = list()
    count = 1
    minimum = 0

    for _ in range(n):
        document, interview = map(int, sys.stdin.readline().split())
        recruitList.append((document, interview))

    recruitList.sort()

    for applicant in recruitList:
        if applicant[0] == 1:
            minimum = applicant[1]
            continue

        if minimum > applicant[1]:
            minimum = applicant[1]
            count += 1

        if minimum == 1:
            break

    print(count)
