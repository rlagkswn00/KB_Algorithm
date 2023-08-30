import sys
input = sys.stdin.readline

# result = list(input().rstrip())
left = list(input().rstrip())
right = []
n = int(input())
# pos = len(result)

for _ in range(n):
    op = input().split()
    if op[0] == 'L':
        if left:
          right.append(left.pop())
        # if pos > 0:
            # pos -= 1
    elif op[0] == 'D':
        # if pos < len(result):
        #     pos += 1
        if right:
            left.append(right.pop())
    elif op[0] == 'B':
        # if pos > 0:
        #     result.remove(result[pos-1]) 
        # O(n) 시간복잡도 - 문제 발생
        if left:
            left.pop()
    elif op[0] == 'P':
        # result.insert(pos)
        # O(n) 시간복잡도 - 문제 발생
        left.append(op[1])

right.reverse()
print("".join(left) + "".join(right))