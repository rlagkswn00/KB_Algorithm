#
# Title: BOJ 15486 퇴사2
# Date: 23.09.03
#
import sys
input = sys.stdin.readline

n = int(input())

# 최초 초기화
dp = [0] * (n+1)
time = [0] * (n+1)
reward = [0] * (n+1)

for i in range(1, n+1):
    time[i], reward[i] = map(int,input().split())


# 1일차부터 n일차 까지 최댓값 계산
for i in range(1, n+1):
    # 현재까지의 최대값과, 전날의 최대값을 비교하여 저장.
    dp[i] = max(dp[i],dp[i-1])
    
    # 끝나는 날짜 설정
    # i일 + 걸리는 시간 - 1
    end = i + time[i] - 1
    if end <= n:
        # 퇴사 전까지 끝낼 수 있는 일정이면 계산 해보고, 아니면 계산 안해도 됨
        # 원래 그날까지 하기로 한 최대값과 (i일 X)
        # 오늘 일을 했을 때의 최대값을 비교 (i일 O)
        dp[end] = max(dp[end], dp[i-1] + reward[i])
        
print(max(dp))
        