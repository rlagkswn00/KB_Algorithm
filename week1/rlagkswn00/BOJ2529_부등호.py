#
# Title: BOJ 2529 부등호
# Theory :
# Date: 23.08.02
#
import sys
input = sys.stdin.readline

# 부등호 개수
k = int(input())
# 부등호 순서
l = input().split()
# 최초 0~9까지 방문 리스트 False * 10개
visited = [False]*10

# 결과값 저장을 위한 max, min 값
mx, mn = "", ""


# 대소비교를 위한 함수
def isOK(i, j, k):
    if k == '<':
        return i < j
    if k == '>':
        return i > j
    return True


# 백트래킹
def dfs(n, s):
    global mx, mn
    # 종료조건 부등호 개수 + 1개 숫자 선정했을 때
    if n == k+1:
        # 작은 숫자부터 탐색하므로, 결과값에 맞는게 탐색되면 min 값 확인
        # min 없으면 가장 작은 숫자임
        # min 있으면 큰 숫자만 업데이트
        # 마지막에 업데이트 되는 숫자가 최고값
        if not len(mn):
            mn = s
        else:
            mx = s
        return

    # 0~9까지 모두 탐색
    for i in range(10):
        # 중복방지
        if not visited[i]:
            # 마지막으로 입력된 숮자(s[-1])과 이번 탐색 숫자(str(i))와 대소문자 l[n-1]을 비교
            # 성립하면 그 숫자 추가 후 다음 자리 탐색
            # n==0 -> 하나도 선택되지 않은 경우 -> s[-1]이 비어있을 때
            if n == 0 or isOK(s[-1], str(i), l[n-1]):
                visited[i] = True
                dfs(n+1, s + str(i))
                visited[i] = False


dfs(0, "")
print(mx)
print(mn)
