import sys

siteN, findN = map(int, sys.stdin.readline().split())
siteDict = dict()
for _ in range(siteN):
    site, pwd = sys.stdin.readline().split()
    siteDict[site] = pwd
for _ in range(findN):
    site = str(sys.stdin.readline().rstrip())
    print(siteDict[site])