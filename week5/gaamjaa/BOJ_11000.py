for k in range(4):
    arr = list(map(int, input().split()))
    si, sj, ei, ej = arr[:4]
    si_2, sj_2, ei_2, ej_2 = arr[4:]

    if ei < si_2 or ej < sj_2 or si > ei_2 or sj > ej_2: #공통X
        print('d')
    elif (si, ej)==(ei_2, sj_2) or (ei, ej)==(si_2, sj_2) or (ei, sj)==(si_2, ej_2) or (si, sj)==(ei_2, ej_2): #점
        print('c') #점(꼭짓점 4개만 맞는 경우)
    elif si == ei_2 or sj == ej_2 or ej == sj_2 or ei == si_2: #선
        print('b')
    else:
        print('a')
