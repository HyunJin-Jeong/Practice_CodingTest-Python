def solution(n):
    fold = 0
    arr = [fold]

    for i in range(n - 1):
        arr = arr + [fold] + [bit ^ 1 for bit in arr[::-1]]

    return arr
