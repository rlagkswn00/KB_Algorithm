L, C = map(int, input().split())
arr = list(input().split())
arr.sort()
output = ['' for _ in range(C)]
answer = []

def dfs(n, cnt, Consonant, Vowel):
    if n == C: #종료조건
        # 정답처리(선택한 개수가 L개, 자음 2개 이상, 모음 1개 이상 선택)
        if cnt == L and Consonant>=2 and Vowel>=1:
            answer.append(''.join(output[i] for i in range(L)))
        return

    #해당 위치의 값을 선택했을 때
    output[cnt] = arr[n]
    if arr[n] in ['a', 'e', 'i', 'o', 'u']: Vowel+=1
    else: Consonant+=1
    dfs(n+1, cnt+1, Consonant, Vowel)

    #해당 위치의 값을 선택하지 않았을 때(위에서 아예 +=로 더해버려서 다시 숫자를 되돌리는 작업을 했습니다)
    if arr[n] in ['a', 'e', 'i', 'o', 'u']: Vowel-=1
    else: Consonant-=1
    dfs(n+1, cnt, Consonant, Vowel)

dfs(0, 0, 0, 0) #현재 arr의 인덱스, 선택한 개수, 자음 개수, 모음 개수

#출력
for ans in answer:
    print(ans)

