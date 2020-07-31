def solution(n):
    fold = 0
    answer = [fold]

    for i in range(n - 1):
        answer = answer + [fold] + [bit ^ 1 for bit in answer[::-1]]

    return answer
