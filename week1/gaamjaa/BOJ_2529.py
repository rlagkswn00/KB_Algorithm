K = int(input())
arr = list(input().split())
output = [0 for _ in range(K+1)]
v = [False for _ in range(10)]
MAX_ANS = "0"
MIN_ANS = "10000000000"

def dfs(n, output):
    global MAX_ANS, MIN_ANS
    if n==K+1:
        if isTrue(output):
            ans = ""
            for t in output:
                ans += str(t)
            if int(MAX_ANS) < int(ans):
                MAX_ANS = ans
            if int(MIN_ANS) > int(ans):
                MIN_ANS = ans
        return;

    for i in range(10):
        if v[i]: continue
        v[i] = True
        output[n] = i
        dfs(n+1, output)
        v[i] = False

def isTrue(output):
    for i in range(K):
        if arr[i] == '<' and output[i]<output[i+1]: continue
        elif arr[i] == '>' and output[i]>output[i+1]: continue
        else: return False
    return True

dfs(0, output)
print(MAX_ANS)
print(MIN_ANS)
