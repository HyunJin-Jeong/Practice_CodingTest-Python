def solution(num):
    for i in range(2, 99):
        try:
            if int(str(num), i) ** 0.5:
                return i
        except ValueError as err:
            pass
print(solution(61))
#N진법으로 표현하는 문법 = int(num, base)
