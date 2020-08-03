def solution(s):
    answer = ''

    for i in range(len(s)):
        cnt = 1
        tmp = s[0:i]
        for j in range(i+1, len(s), i+1):
            if tmp == s[j:j+i]:
                cnt += 1
            else:
                answer += str(cnt) + tmp
                cnt = 1

    return answer

i = 1
s[0:1] = ab
ab == s[0:0+1] == ab? yes cnt +1
ab == s[j+i=:] == ba? no answer += 2ab
