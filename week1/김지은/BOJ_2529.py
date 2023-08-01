import sys

k = int(sys.stdin.readline())
list = input().split()
num = []
max_v = '0'
min_v = '999999999'
def dfs(idx,n):
    global k, max_v, min_v
    if n>1:
        if list[n-2]=='<': # 항상 마지막 연산자만 갖고 체크
            if num[n-1]-num[n-2] <0:
                return
        else:
            if num[n-1]-num[n-2] >0:
                return
    if n == k+1:
        value = ''.join(map(str, num))
        max_v = max(max_v,value)
        min_v = min(min_v,value)
        return

    for i in range(10):
        if i not in num: #한번도 안쓰인 숫자를 사용
            num.append(i)
            dfs(i+1,n+1)
            num.pop()
            

dfs(0,0)
print(max_v)
print(min_v) 
                