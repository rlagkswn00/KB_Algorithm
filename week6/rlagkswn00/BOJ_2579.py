#
# Title: BOJ 2579 계단 오르기
# Theory : DP
# Date: 23.00.02
#
import sys
input = sys.stdin.readline

n = int(input())
# 계단 입력
steps = [0]
for _ in range(n):
    steps.append(int(input()))
# 개수가 3 이하인 경우에는 다 밟으면 되므로
# 전부 합쳐서 출력 후 종료
if n <= 2:
    print(sum(steps))
    exit(0)
# 초기화
dp = [0] * (n+1);

# 초기값 설정
dp[1] = steps[1]
dp[2] = steps[2] + steps[1] #무조건 한칸단위로 밟은게 더 큼

# 3번째 계단부터 마지막 계단까지 DP 계산
# dp[i-3] + steps[i-1] + steps[i] : ... X O O : 전칸을 밟은 경우
# dp[i-3] : 세칸 전을 밟고 한칸 쉰 경우라는 뜻.
# dep[i-2] + steps[i] : ... O X O -> 2칸 건너뛴 경우
for i in range(3,n+1):
    dp[i] = max(dp[i-3] + steps[i-1] + steps[i], dp[i-2] + steps[i])
print(dp[-1])