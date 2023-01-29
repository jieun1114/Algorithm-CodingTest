from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def dfs(place, x, y, visit):
    dq = deque()
    dq.append([x, y, 0])

    while dq:
        a, b, dist = dq.popleft()
        visit[a][b] = 1

        if place[a][b] == 'P':
            if 0 < dist <= 2:
                return False
            else:  # P를 만날경우 다시 시작
                dist = 0

        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]
            if 0 <= na < 5 and 0 <= nb < 5:
                if visit[na][nb] == 0 and place[na][nb] != 'X':
                    dq.append([na, nb, dist + 1])

    return True


def solution(places):
    answer = []

    for place in places:
        visit = [[0] * 5 for _ in range(5)]
        flag = True
        for x in range(5):
            for y in range(5):
                if place[x][y] == 'P' and visit[x][y] == 0:
                    if not dfs(place, x, y, visit):
                        flag = False
                        break
            if not flag:
                break

        if flag:
            answer.append(1)
        else:
            answer.append(0)

    return answer