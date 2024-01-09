import sys


n = int(input())
towerList = list(map(int, sys.stdin.readline().split()))
answer = [0] * n
# 타워의 최대 높이 : 10 ** 8 (10의 8승)
# towerStack의 값들은 (탑의 높이, 탑의 위치) 튜플 형태로 저장
# towerStack의 초기값을 타워의 최대 높이보다 하나 더 높게 설정하고 위치값을 0으로 설정하여 첫 번째 타워가 인덱스 1에 비교할 타워 높이가 있도록 설정
towerStack = [(10 ** 8 + 1, 0)]

for i in range(n):
    currentHeight = towerList[i]
    # 현재 위치보다 왼쪽에 있는 탑 중, 더 낮은 탑은 더이상 비교할 필요가 없기 때문에 pop()으로 삭제
    # towerStack의 마지막 인덱스에서 튜플의 첫 번째 인자(= 탑의 높이)와 비교
    while towerStack[-1][0] < currentHeight:
        towerStack.pop()
    # while문 탐색이 끝남 = towerStack의 마지막 값이 현재 탑의 높이보다 큰 탑
    # towerStack이 비어 잇ㅈ지 않는 이유 : (10 ** 8 + 1, 0)으로 초기값을 설정했기 때문

    answer[i] = towerStack[-1][1] # towerStack의 마지막 인덱스에서 튜플의 두 번째 인자(탑의 위치) 대입
    towerStack.append((currentHeight, i + 1))

print(*answer)
