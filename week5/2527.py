import sys
input = sys.stdin.readline

for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int, input().split())
    if p1 < x2 or p2 < x1 or y1 > q2 or q1 < y2:
        print('d')
        continue
    elif x1==p2 or x2==p1:
        if q1==y2 or q2==y1:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1==y2 or q2==y1:
            print('b')
            continue
    else:
        print('a')
        continue

    # import sys

# ans = []
# for _ in range(4):
#     inputs = list(map(int, sys.stdin.readline().split()))
#     first_x1 = inputs[0]
#     first_x2 = inputs[2]
#     first_y1 = inputs[1]
#     first_y2 = inputs[3]

#     second_x1 = inputs[4]
#     second_x2 = inputs[6]
#     second_y1 = inputs[5]
#     second_y2 = inputs[7]

#     first_x_len = first_x2 - first_x1
#     second_x_len = second_x2 - second_x1
#     first_y_len = first_y2 - first_y1
#     second_y_len = second_y2 - second_y1

#     if first_x1 == second_x1 and first_x2 == second_x2 and first_y1 == second_y1 and first_y2 == second_y2:
#         ans.append('a')
#     elif first_x1 <= second_x1:
#         if second_x2 - first_x1 > (first_x_len + second_x_len):
#             ans.append('d')
#         elif second_x2 - first_x1 == (first_x_len + second_x_len):
#             if first_y2 < second_y1 or first_y1 > second_y2:
#                 ans.append('d')
#             elif first_y2 == second_y1 or first_y1 == second_y2:
#                 ans.append('c')
#             else:
#                 ans.append('b')
#         else:
#             ans.append('a')
#     else:
#         if first_x2 - second_x1 > (first_x_len + second_x_len):
#             ans.append('d')
#         elif first_x2 - second_x1 == (first_x_len + second_x_len):
#             if first_y2 < second_y1 or first_y1 > second_y2:
#                 ans.append('d')
#             elif first_y2 == second_y1 or first_y1 == second_y2:
#                 ans.append('c')
#             else:
#                 ans.append('b')
#         else:
#             ans.append('a')


# for result in ans:
#     print(result)