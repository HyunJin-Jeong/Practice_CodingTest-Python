def solution(phone_book):
    leng = len(phone_book)
    for i in range(leng):
        for j in range(leng):
            if phone_book[i] in phone_book[j][:len(phone_book[i])] and i != j:
                return False
    return True

'''
def solution(phone_book):
    phone_book = sorted(phone_book)
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
    return True
'''

print(solution(['119','97674223','1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))
