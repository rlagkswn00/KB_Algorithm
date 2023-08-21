N = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort(reverse=True)

ANS = 0
for i in range(len(arr1)):
    ANS += arr1[i]*arr2[i]

print(ANS)
