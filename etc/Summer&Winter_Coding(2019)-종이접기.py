def solution(n):
    fold = 0
    answer = [fold]

    for i in range(n - 1):
        answer = answer + [fold] + [sw ^ 1 for sw in answer[::-1]]

    return answer
