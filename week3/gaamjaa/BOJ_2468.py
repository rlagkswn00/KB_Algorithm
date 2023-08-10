from collections import deque

N = int(input())
MIN_HEIGHT = 101
MAX_HEIGHT = 0

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

arr = []
# 입력하면서 이 지역의 최대 높이와 최소 높이를 저장한다
for _ in range(N):
    tmp = list(map(int, input().split()))
    MIN_HEIGHT = min(min(tmp), MIN_HEIGHT)
    MAX_HEIGHT = max(max(tmp), MAX_HEIGHT)
    arr.append(tmp)

def bfs(v, si, sj, h):
    q = deque()
    q.append([si, sj])
    v[si][sj] = True

    while q:
        ci, cj = q.popleft()
        for i in range(4):
            ni = di[i] + ci
            nj = dj[i] + cj
            if 0<=ni<N and 0<=nj<N: # 범위 체크
                if not v[ni][nj] and arr[ni][nj]>h: # 방문 체크 + 내린 비보다 높은 지대
                    v[ni][nj] = True
                    q.append([ni, nj])

ans = 0
# 비가 올 수 있는 모든 경우를 확인한다 (가장 낮은 높이-1 ~ 가장 높은 높이+1 : 하나도 잠기지 않는 경우도 봐야하기 때문)
for h in range(MIN_HEIGHT-1, MAX_HEIGHT+1):
    v = [[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j]>h: 
            # 지역의 높이가 내린 비보다 높아야 안전지대 + 방문확인 (bfs 밖에서 cnt를 해야 안전지대의 개수를 볼 수 있으므로 v 배열을 밖에 선언)
                bfs(v, i, j, h)
                cnt += 1
    ans = max(cnt, ans) # 안전지대의 max를 ans에 저장

print(ans)
