def solution(s):
    min = float('inf')
    cnt = 1

    for i in range(1, len(s)+1):
        tmp = s[0:i]
        comp = ''

        for j in range(i, len(s)+1, i):
            if tmp == s[j:j+i]:
                cnt += 1

            elif cnt == 1:
                comp += tmp
                tmp = s[j:j+i]

            else:
                comp += str(cnt) + tmp
                tmp = s[j:j+i]
                cnt = 1

        if len(s) % i != 0:
            comp += s[:-(len(s) % i)]

        print(comp)

        if min > len(comp):
            min = len(comp)

    return min
