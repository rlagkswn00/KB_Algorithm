import sys
from collections import deque

left = list(input())
right = []

N = int(input())
arr = [list(sys.stdin.readline().rstrip().split()) for _ in range(N)]

# 초기 커서는 문장 맨 뒤에 위치
# L: 커서 왼쪽으로 / D: 커서 오른쪽 / B: 왼쪽 문자 삭제 / P $: $문자 커서 왼쪽에 추가

cursor = len(left)

for a in arr:
    if a[0] == 'L':
        if len(left) > 0:
            right.append(left.pop())
    elif a[0] == 'D':
        if len(right) > 0:
            left.append(right.pop())
    elif a[0] == 'B':
        if len(left) > 0:
            left.pop()
    else:
        left.append(a[1])
    # print(left, right)

print(''.join(left)+''.join(reversed(right)))
