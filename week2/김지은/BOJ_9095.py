
def dfs(sum,n):
    global cnt
    if sum > n: # 숫자보다 커진 경우 재귀함수 호출 막기
        return 

    if sum == n:
        cnt+=1
        return 
    
    dfs(sum+1,n) #1 을 선택했을 때
    dfs(sum+2,n) #2 를 선택했을 때
    dfs(sum+3,n) #3을 선택했을 때

t = int(input())
cnt = 0

for _ in range(t):
    cnt=0
    n = int(input())
    dfs(0,n)
    print(cnt)