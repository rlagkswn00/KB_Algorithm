import sys
import heapq

n = int(sys.stdin.readline())
arr=[]
classes=[]

start = 0
end =0
cnt = 1

for _ in range(n):
    s,e=map(int,sys.stdin.readline().split())
    heapq.heappush(arr,(e,s))

e,s = heapq.heappop(arr)
heapq.heappush(classes,e)

while arr:
    end = classes[0]
    if s < end: 
        cnt += 1
    else:
        start=s
        end=e
print(cnt)


# import heapq
# n = int(input())

# q = []

# for i in range(n):
#     start, end = map(int, input().split())
#     q.append([start, end])

# q.sort()

# room = []
# heapq.heappush(room, q[0][1])

# for i in range(1, n):
#     if q[i][0] < room[0]: # 현재 회의실 끝나는 시간보다 다음 회의 시작시간이 빠르면
#         heapq.heappush(room, q[i][1]) # 새로운 회의실 개설
#     else: # 현재 회의실에 이어서 회의 개최 가능
#         heapq.heappop(room) # 새로운 회의로 시간 변경을 위해 pop후 새 시간 push
#         heapq.heappush(room, q[i][1])

# print(len(room))