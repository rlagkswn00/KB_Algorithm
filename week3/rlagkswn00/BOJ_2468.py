#
# Title: BOJ 2468 안전영역
# Theory : 
# Date: 23.08.10
#
import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]

maxCnt = 0

# for _ in range(N):
    # board.append(list(map(int,input().split())))

#위 대신 아래와 같이 적용 가능하다.
#리스트 컴프리헨션
# 리스트를 쉽게 짧게 한줄로 만들 수 있는 파이썬 문법 
board = [list(map(int,input().split())) for _ in range(N)]

def bfs(x,y):
    q = deque()
    q.append([x,y])
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 > nx or nx >= N or 0 > ny or ny >= N:
                continue
            if visited[nx][ny]:
                continue
            
            visited[nx][ny] = True
            q.append([nx,ny])


for i in range(101):
    visited = [[False] * N for _ in range(N)]
    cnt = 0
    for j in range(N):
        for k in range(N):
            if board[j][k] <= i:
                visited[j][k] = True
    for j in range(N):
        for k in range(N):
            if not visited[j][k]:
                visited[j][k] = True
                bfs(j,k)
                cnt += 1
    
    if cnt == 0:
        break;
    
    maxCnt = max(maxCnt,cnt)
    
print(maxCnt)