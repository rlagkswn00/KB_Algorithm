#
# Title: BOJ 1018 체스판 다시 칠하기
# Theory :
# Date: 23.07.31
#
import sys
input = sys.stdin.readline

board = []
wb = [
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW"
]
bw = [
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB",
    "BWBWBWBW",
    "WBWBWBWB"
]


def bwCnt(l, m):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (board[l + i][m + j] != bw[i][j]):
                cnt += 1
    return cnt


def wbCnt(l, m):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (board[l + i][m + j] != wb[i][j]):
                cnt += 1
    return cnt


min_val = 9999999
x, y = map(int, input().split())

for i in range(x):
    board.append(input())

for i in range(0, x-8 + 1):
    for j in range(0, y-8 + 1):
        tmp = min(wbCnt(i, j), bwCnt(i, j))
        if (tmp < min_val):
            min_val = tmp
print(min_val)
