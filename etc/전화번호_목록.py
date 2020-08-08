def solution(phone_book):
    leng = len(phone_book)
    for i in range(leng):
        for j in range(leng):
            if phone_book[i] in phone_book[j][:len(phone_book[i])] and i != j:
                return False
    return True

print(solution(['119','97674223','1195524421']))
print(solution(['123','456','789']))
print(solution(['12','123','1235','567','88']))
