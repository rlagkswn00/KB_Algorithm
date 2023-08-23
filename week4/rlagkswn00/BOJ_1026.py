#
# Title: BOJ 1026 보물
# Theory : 
# Date: 23.08.10
#
# sys import
import sys
input = sys.stdin.readline

# 입력
n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))

# 정렬
a.sort(reverse=True)
b.sort()

result = 0
for i in range(n):
    # result += a[i] * b[i]
    result += min(a) * max(b)
    a.pop(a.index(min(a)))
    b.pop(b.index(max(b)))

print(result)