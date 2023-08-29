import sys

n = int(sys.stdin.readline())
arr1=list(map(int, sys.stdin.readline().split()))
arr2=list(map(int, sys.stdin.readline().split()))

arr1.sort()
arr2.sort(reverse=True)
sum=0
for i in range(len(arr1)):
    sum+= arr1[i]*arr2[i]
print(sum)

#다른 풀이
# n = int(input())

# a_list = list(map(int, input().split()))
# b_list = list(map(int, input().split()))

# s = 0
# for i in range(n):
#     s += min(a_list) * max(b_list)
#     a_list.pop(a_list.index(min(a_list)))
#     b_list.pop(b_list.index(max(b_list)))

# print(s)

