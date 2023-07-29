import sys
from collections import deque

dx = [-2,-2,-1,-1,1,1,2,-1]
dy = [-1,1,-2,2,-2,2,-1,1]

def bfs(sx,sy,ex,ey):
    dq = deque()
    dq.append([sx, sy])
    chess[sx][sy] = 1

    while dq:
        x, y = dq.popleft()
        if x == ex and y == ey:
            print(chess[x][y]-1)
            return

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < L and 0 <= ny < L and chess[nx][ny] == 0:
                dq.append([nx, ny])
                chess[nx][ny] = chess[x][y]+1

T = int(sys.stdin.readline())
for _ in range(T):
    L = int(sys.stdin.readline())
    sx, sy = map(int, sys.stdin.readline().split())
    ex, ey = map(int, sys.stdin.readline().split())
    chess = [[0] * L for _ in range(L)]
    bfs(sx, sy, ex, ey)


