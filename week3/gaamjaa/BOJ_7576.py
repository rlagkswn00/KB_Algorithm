from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

# 상 하 좌 우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

# 익은 토마토 위치 담기
s_tomato = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
           s_tomato.append([i, j])

def bfs(s_tomato):
    # q 선언 및 v 배열 선언
    q = deque()
    v = [[False] * M for _ in range(N)]

    # 시작 위치 모두 넣기
    for s in s_tomato:
        s.append(0) #날짜도 배열에 추가해서 q에 넣기
        q.append(s)
        v[s[0]][s[1]] = True #처음 위치 방문 표시

    ci = cj = cday = 0 #마지막 값 리턴을 위해 cday 변수를 while 밖에서 선언
    while q:
        ci, cj, cday = q.popleft()
        for i in range(4): #4방향 방문
            ni = di[i] + ci
            nj = dj[i] + cj
            if 0 <= ni < N and 0 <= nj < M:
                if not v[ni][nj] and arr[ni][nj] == 0: 
                    #(방문X + 안익은 토마토)면 방문 표시 및 q에 추가
                    v[ni][nj] = True
                    q.append([ni, nj, cday+1])

    #안익은 토마토인데 방문하지 않았으면 -1 리턴
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and not v[i][j]:
                return -1
    return cday

print(bfs(s_tomato))
