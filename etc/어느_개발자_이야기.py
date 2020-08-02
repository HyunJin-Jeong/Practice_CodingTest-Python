def solution(num):
    for i in range(2, 100):
        result = 0

        for j in range(len(num)):
            result += (int(num[-(j+1)]) * (i ** j))

        if result ** 0.5 == int(result ** 0.5):
            return i

print(solution(input()))
