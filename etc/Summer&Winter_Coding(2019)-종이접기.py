def solution(n):
    answer = [0]

    for i in range(n - 1):
        answer = answer + [0] + [sw ^ 1 for sw in answer[::-1]]

    return answer

print(solution(4))
