import sys
input = sys.stdin.readline

def dfs(sum):
    global k
    if sum > k:
        return
    
    if sum == k:
        global cnt
        cnt+=1
        return
    
    for i in range(3):
        dfs(sum + i + 1)


T = int(input())
k = 0
cnt = 0
while T :
    T-=1
    k = int(input())
    
    dfs(0)

    print(cnt)
    k = 0
    cnt = 0

