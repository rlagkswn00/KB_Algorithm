import sys

l, c = map(int, sys.stdin.readline().split())

k = sys.stdin.readline()
list = k.split()
list.sort() # 알파벳순 정렬
arr=[]

def checkVowel(arr): # 모음이 1개이상, 자음이 2개이상
    cnt=0
    for alph in arr:
        if alph in ('a', 'e', 'i', 'o', 'u') :
            cnt+=1

    if cnt>=1 and l-cnt>=2: #전체에서 모음 수 빼면 자음수
        return True
    return False

def dfs(idx,depth):
    if depth == l:
        if checkVowel(arr):
            print("".join(arr))
        return
    for i in range(idx,c):
        if list[i] not in arr:
            arr.append(list[i])
            dfs(i+1,depth+1)
            arr.pop()

          
        
dfs(0,0)



