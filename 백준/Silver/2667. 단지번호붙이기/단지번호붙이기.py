import sys

n = int(input())
dx = [0, 0, 1, -1]  # 탐색 위치를 상하로 바꾸기 위한 자료
dy = [1, -1, 0, 0]  # 탐색 위치를 좌우로 바꾸기 위한 자료
complex = []
complexCount = []

for _ in range(n):
    complex.append(list(map(int, sys.stdin.readline().strip())))

for row in range(n):
    for col in range(n):
        if complex[row][col] != 1:
            continue

        count = 1
        stack = [(row, col)]
        complex[row][col] = 0

        while stack:
            x, y = stack.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or complex[nx][ny] != 1:
                    continue
                stack.append((nx, ny))
                complex[nx][ny] = 0
                count += 1

        complexCount.append(count)

complexCount.sort()
print(len(complexCount))
for i in complexCount:
    print(i)
