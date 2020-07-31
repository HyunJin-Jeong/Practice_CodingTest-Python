def reverse(list):
    return [bit ^ 1 for bit in list[::-1]]

def solution(n):
    answer = [0]
    if (n > 1):
        for i in range(2, n + 1):
            answer = answer + [0] + reverse(answer)
    return answer
