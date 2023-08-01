N, M = map(int, input().split())
board = []
count = []

for _ in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        firstW = 0
        firstB = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W': #첫번째 시작이 W인 경우, (라고 가정했지만 W가 아니라면 색칠해야 하니까 firstW++)
                        firstW += 1
                    if board[k][l] != 'B':
                        firstB += 1
                else:
                    if board[k][l] != 'B': #그 옆은 B로 칠해져야 한다.
                        firstW += 1
                    if board[k][l] != 'W':
                        firstB += 1
        count.append(min(firstW, firstB))

print(min(count))
