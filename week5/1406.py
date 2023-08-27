import sys
from collections import deque

arr_before_cursor = deque(input())
arr_after_cursor = deque() # 두개의 stack 이용
n = int(sys.stdin.readline())

for _ in range(n):
    inputs = sys.stdin.readline().split()
    command = inputs[0]

    if command == "L":
        if arr_before_cursor: # 커서가 맨 앞이 아닐때
            arr_after_cursor.appendleft(arr_before_cursor.pop())
    elif command == "D":
        if arr_after_cursor: # 커서가 맨 뒤가 아닐때
            arr_before_cursor.append(arr_after_cursor.popleft())
    elif command == "B":
        if arr_before_cursor: # 커서가 맨 앞이 아닐때
            arr_before_cursor.pop()
    elif command == "P":
        char = inputs[1]
        arr_before_cursor.append(char)

result = ''.join(arr_before_cursor) + ''.join(arr_after_cursor)
print(result)
