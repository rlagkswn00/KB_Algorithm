#
# Title: BOJ 7576 토마토
# Theory : 
# Date: 23.08.10
#
import sys
input = sys.stdin.readline
from collections import deque # list 대신 덱 사용 - 더빠르다고 함..

M, N = map(int,input().split())
#리스트 컴프리헨션으로 입력
board = [list(map(int,input().split())) for _ in range(N)]

x = 0
y = 0
cnt = 0
isOK = False;
# 큐생성 bfs
q = deque()

# 시작지점 찾기
# 0이 하나도 없는지 확인(모두 다 익은 토마토인지))
for i in range(N):
    for j in range(M):
        if board[i][j] == 1:
            q.append([i,j])
        if not isOK and board[i][j] == 0:
            isOK = True

# 하나도 0 이 없다면 끗
if not isOK:
    print(0)
    exit()



dx = [0,0,-1,1]
dy = [-1,1,0,0]

while q:
    x,y = q.popleft();
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 > nx or nx >= N or 0 > ny or ny >= M:
            continue
        
        if board[nx][ny] != 0:
            continue
        board[nx][ny] = board[x][y] + 1
        q.append([nx,ny])

result = 0
for b in board:
    if 0 in b:
        print(-1)
        exit()
    result = max(result,max(b))
    
print(result-1)