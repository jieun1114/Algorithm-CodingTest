#Two Dots
import sys
sys.setrecursionlimit(10**7)

n, m = map(int, sys.stdin.readline().split())
dots = [list(input().rstrip()) for _ in range(n)]
# dots = []
# for i in range(n):
#     temp = list(str(sys.stdin.readline().strip()))
#     dots.append(temp)

visit = [[0]*m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(color, x,y,cnt):

    #print(color,x,y,cnt)

    if sx==x and sy==y and cnt >=4:
        print("Yes")
        exit()

    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if 0<=nx<n and 0<=ny<m and dots[nx][ny] == color:
            if visit[nx][ny] == 0:
                visit[nx][ny] = 1
                dfs(color,nx,ny,cnt+1)
                visit[nx][ny] = 0

for i in range(n):
    for j in range(m):
        if visit[i][j] == 0:
            sx, sy = i, j
            dfs(dots[i][j],i,j,1)

print("No")

