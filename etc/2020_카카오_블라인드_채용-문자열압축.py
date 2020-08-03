def solution(s):
    min = float('inf')
    
    for i in range(1, len(s)+1):
        tmp = s[0:i]
        comp = ''
        cnt = 1

        for j in range(i, len(s)+1, i):
            if tmp == s[j:j+i]:
                cnt += 1

            elif cnt == 1:
                comp += tmp

            else:
                comp += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1

        if min > len(comp):
            min = len(comp)

    return min
