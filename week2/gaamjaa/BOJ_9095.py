T = int(input())
N = 0; ANS = 0

def dfs(n, result): #선택횟수(사실 필요 없어요), 더한결과
    global N, ANS
    if result >= N:
        if result == N:
            ANS += 1
        return
    dfs(n+1, result+1) #1 더하기
    dfs(n+1, result+2) #2 더하기
    dfs(n+1, result+3) #3 더하기 중 하나를 무조건 선택 (조합의 느낌과 비슷)

for tc in range(T):
    N = int(input())
    ANS = 0
    dfs(0, 0)
    print(ANS)

