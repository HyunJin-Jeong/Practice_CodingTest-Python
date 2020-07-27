def solution(board, moves):
    answer = 0
    bucket = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i - 1] != 0:
                bucket.append(board[j][i - 1])
                board[j][i - 1] = 0
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    del bucket[-1]
                    del bucket[-1]
                    answer += 2
                break
    return answer

test = [1,2,3,4,5]
print(test[:-2])
print(test[-1:-2])
print(test[-2:])
