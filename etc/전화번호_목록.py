def solution(phone_book):
    for i in range(0, len(phone_book)):
        for j in range(0, len(phone_book)):
            if str(phone_book[i]) in str(phone_book[j]) and i != j:
                return False
    return True


print(solution([119, 97674223, 1195524421]))
print(solution([123,456,789]))
print(solution([12,123,1235,567,88]))
