def solution(num):
    for i in range(2,99):
        for j in range(2,99):
            tmp = str(j ** 2)
            try:
                if num == int(tmp, i):
                    return i
            except ValueError as err:
                pass
                
print(solution(15))
#N진법으로 표현하는 문법 = int(num, base)
