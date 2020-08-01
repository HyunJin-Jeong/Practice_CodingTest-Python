def solution(num):
    print(int(str(num), 10) ** 0.5)

    '''
    for i in range(2, 99):
        try:
            if int(str(num), 10) ** 0.5:
                print(i)
        except ValueError as err:
            pass
    '''
print(solution(15))
#N진법으로 표현하는 문법 = int(num, base)
