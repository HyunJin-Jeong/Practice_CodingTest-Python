def solution(num):
    num = num[::-1]
    
    for i in range(2, 100):
        result = 0
        cnt = 0

        for j in range(len(num)):
            if int(num[j]) < i:
                result += int(num[j]) * (i ** j)
                cnt += 1
            else:
                break

        if len(num) == cnt and result ** 0.5 == int(result ** 0.5):
            return i

print(solution(input()))
