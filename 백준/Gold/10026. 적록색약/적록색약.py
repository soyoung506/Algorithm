import sys

n = int(input())
colorList = list()
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
visited1 = [[False for _ in range(n)] for _ in range(n)]
visited2 = [[False for _ in range(n)] for _ in range(n)]
count1 = 0
count2 = 0

for _ in range(n):
    colorList.append(list(sys.stdin.readline().strip()))

for row in range(n):
    for col in range(n):
        if visited1[row][col]:
            continue

        count1 += 1
        stack = [(row, col)]
        visited1[row][col] = True

        while stack:
            x, y = stack.pop()
            color = colorList[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or colorList[nx][ny] != color or visited1[nx][ny]:
                    continue
                stack.append((nx, ny))
                visited1[nx][ny] = True

for row in range(n):
    for col in range(n):
        if visited2[row][col]:
            continue

        count2 += 1
        stack = [(row, col)]
        visited2[row][col] = True

        while stack:
            x, y = stack.pop()
            color = colorList[x][y]
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx < 0 or nx >= n or ny < 0 or ny >= n or visited2[nx][ny]:
                    continue
                if not (colorList[nx][ny] == 'B' or color == 'B'):
                    colorList[nx][ny] = color
                if colorList[nx][ny] != color:
                    continue
                stack.append((nx, ny))
                visited2[nx][ny] = True

answer = [count1, count2]
print(' '.join(str(num) for num in answer))
