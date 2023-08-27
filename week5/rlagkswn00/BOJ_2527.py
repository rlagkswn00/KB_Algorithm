import sys
input = sys.stdin.readline

result = ""
for _ in range(4):
    x1,y1,p1,q1,x2,y2,p2,q2 = map(int,input().split())
    
    # 공통부분 없음
    if (p1 < x2) or (x1 > p2) or (q1 < y2) or (y1 > q2):
        # result += 'd'
        print('d')
    # 점일치
    elif (x1 == p2 and y1 == q2) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2):
        # result += 'c'
        print('c')
    # 선분일치
    elif (p1 == x2) or (x1 == p2) or (y1 == q2) or (q1 == y2):
        # result += 'b'
        print('b')
    # 그외 겹침
    else:
        # result += 'a'
        print('a')
# print(result)