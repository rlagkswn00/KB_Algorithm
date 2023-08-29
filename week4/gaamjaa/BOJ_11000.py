import sys
import heapq

N = int(sys.stdin.readline().rstrip())
arr = []
pre = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().rstrip().split())))

arr.sort(key=lambda x:x[0]) #key=lambda x:(x[1],x[0])

heapq.heappush(pre, arr[0][1])

for i in range(1, N):
    if pre[0] > arr[i][0]:
        heapq.heappush(pre, arr[i][1])
        continue
    heapq.heappop(pre)
    heapq.heappush(pre, arr[i][1])

print(len(pre))
