import sys
from collections import deque #deque 안쓰면 시간초과 발생

n = int(sys.stdin.readline())
arr = [list(map(int, input().split())) for _ in range(n)]

q= deque()

dx = [-1,1,0,0]
dy=[0,0,-1,1]


max_v = max(map(max, arr)) # 최대 높이
min_v = min(map(min, arr)) # 최소 높이
ans = -1

def bfs(i,j,cnt):
 
    q.append((i,j))
    isVisited[i][j]=cnt

    while(len(q)>0):
        cur_x,cur_y = q.popleft()
        
        for k in range(4):
            new_x = cur_x + dx[k]
            new_y = cur_y + dy[k]
            if(new_x>n-1 or new_y>n-1 or new_x<0 or new_y<0): continue
            if arr[new_x][new_y]>=max_v and isVisited[new_x][new_y]==0:
                isVisited[new_x][new_y] = cnt
                q.append((new_x,new_y))

while(max_v>=min_v):

    isVisited = [[0 for _ in range(n)] for _ in range(n)]
    cnt=0 # 안전영역 개수 세기

    for i in range(n):
        for j in range(n):
            if arr[i][j]>=max_v and isVisited[i][j]==0:
                cnt+=1 #이전에 bfs를 모두 마치고 cnt 증가시키기
                bfs(i,j,cnt)
                
    ans = max(cnt,ans)

    
    max_v-=1

print(ans)




