import sys
from collections import deque

n = int(input())
chessList = list()
answer = []
dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

for _ in range(n):
    chessSize = int(input())
    knightX, knightY = map(int, sys.stdin.readline().split())
    moveX, moveY = map(int, sys.stdin.readline().split())
    visited = [[False for _ in range(chessSize)] for _ in range(chessSize)]
    visited[knightX][knightY] = True
    count = 0
    q = deque([(knightX, knightY)])
    flag = True

    while flag:
        if knightX == moveX and knightY == moveY:
            break
        count += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for i in range(8):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx == moveX and ny == moveY:
                    flag = False
                    break
                if nx < 0 or nx >= chessSize or ny < 0 or ny >= chessSize or visited[nx][ny]:
                    continue
                q.append((nx, ny))
                visited[nx][ny] = True

            if not flag:
                break

    answer.append(count)

for i in answer:
    print(i)
