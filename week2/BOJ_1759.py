import sys
input = sys.stdin.readline

L,C = map(int,input().split())
li = input().split()
visited = [False] * C

li.sort()

def dfs(n, res, next):
    if n == L:
        cnt = 0
        for i in res:
            if i == 'a' or i == 'u' or i == 'i' or i == 'e' or i == 'o':
                cnt+=1
        
        if cnt >= 1 and (len(res) - cnt >= 2):
            print(res)
        return
    
    for i in range(next,len(li)):
        if visited[i]:
            continue
        visited[i] = True
        dfs(n+1,res + li[i], i)
        visited[i] = False

dfs(0,"",0)