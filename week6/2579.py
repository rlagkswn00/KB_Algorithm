n=int(input())
stair=[int(input()) for _ in range(n)] 
dp=[0]*(n) 
if n<=2:
    print(sum(stair))
else: 
    dp[0]=stair[0] # 첫째 계단 수동 계산
    dp[1]=stair[0]+stair[1] # 둘째 계단까지 수동 계산
    for i in range(2,n): # 3번째 계단 부터 dp 점화식 이용해서 최대값 구하기
        dp[i]=max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])
    print(dp[-1])

# import sys
# input = sys.stdin.readline

# n = int(input())
# stairs = [0] + list(int(input()) for _ in range(n))

# dp = [[0,0] for _ in range(n+1)]
# dp[1] = [stairs[1], stairs[1]]

# for i in range(2,n+1):
#     dp[i][0] = stairs[i] + max(dp[i-2][0], dp[i-2][1])
#     dp[i][1] = stairs[i] + dp[i-1][0]

# print(max(dp[n]))