import sys

def play(x,y):
    cnt =0 
    for i in range(8):
        for j in range(8):
            if chess[i][j]!=board[x+i][y+j]: #하나라도 다르면 다시 색칠해줘야함.
                cnt+=1
    return min(cnt,64-cnt) # 두 가지 경우의 수 모두 고려. 


chess=[['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']] 

# 1. 'W' 로 시작하는 경우의 수 2. 'B' 로 시작하는 경우의 수

n, m = map(int, sys.stdin.readline().split())
ans = n*m

board = [list(map(str, input())) for _ in range(n)]  

for i in range(n-7):
    for j in range(m-7): 
        value = play(i,j)
        ans = min(ans,value) #여러가지 8x8 체스판 경우의 수 중에서 최소값 구하기
print(ans)

#bfs로 풀어서 색깔이 같으면 색('B'->'W')을 바꿔주는 방식으로도 도전을 해봤는데 예외사항이 너무 많아서 완전탐색이 더 쉬운 것 같다.