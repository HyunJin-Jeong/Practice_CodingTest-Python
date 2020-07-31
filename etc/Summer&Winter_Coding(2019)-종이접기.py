def solution(n):
    v = 0
    answer = [v]

    for i in range(n - 1):
        answer = answer + [v] + [sw ^ 1 for sw in answer[::-1]]

    return answer
