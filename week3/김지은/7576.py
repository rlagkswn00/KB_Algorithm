import sys
from collections import deque #deque 안쓰면 시간초과 발생

n, m = map(int, sys.stdin.readline().split())


arr = [list(map(int, input().split())) for _ in range(m)]
isVisited = [[0 for _ in range(n)] for _ in range(m)]

q = deque()
dx=[-1,1,0,0]
dy=[0,0,-1,1]

isAllRipe = True

def bfs():
  
    while(len(q)!=0):
        
        cur_x, cur_y = q.popleft()
      
        for i in range(4):
            new_x = cur_x + dx[i]
            new_y = cur_y + dy[i]

            if (new_x > m-1 or new_x <0 or new_y>n-1 or new_y <0): continue
            if (arr[new_x][new_y]==1 or arr[new_x][new_y]==-1 ): continue
            if (isVisited[new_x][new_y]==0 and arr[new_x][new_y]==0): 
                isVisited[new_x][new_y]= isVisited[cur_x][cur_y]+1
                q.append((new_x,new_y))

if all(0 not in _ for _ in arr):  # 저장될 때부터 모든 토마토가 익어있는 상태이면 0을 출력
    print(0)
else:
    for i in range(m):
        for j in range(n):
            if arr[i][j]==1:
               isVisited[i][j] = 1
               q.append((i,j)) # 바로 bfs 호출하면 익는 날짜가 동시적으로 진행이 되지 않아서 큐에 삽입해서 시작한다.
    bfs()
    for i in range(m): # 만약 익지 않은 토마토인데 -1로 감싸져서 방문을 못했으면 -1 출력
        for j in range(n):
            if arr[i][j]==0 and isVisited[i][j]==0:
                isAllRipe = False
                break
    if isAllRipe:
        print(max(map(max, isVisited))-1)    
    else:
        print(-1)



