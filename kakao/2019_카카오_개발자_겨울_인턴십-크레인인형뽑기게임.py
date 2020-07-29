def solution(board, moves):

    # 터트린 인형의 수와 인형을 담기 위한 바구니 변수를 생성합니다.
    answer = 0; bucket = []

    # moves 배열 순서에 따라 진행됩니다.
    for i in moves:

        # 크레인은 게임화면(board)의 세로 길이만큼 내려갈 수 있습니다.
        # 크레인이 인형(0 외의 정수)을 만나면 바구니에 옮기고 그 자리는 빈 공간(0)이 됩니다.
        for j in range(0, len(board)):
            if board[j][i - 1] != 0:
                bucket.append(board[j][i - 1])
                board[j][i - 1] = 0

                # 바구니에 같은 값이 연속 두 번 옮겨지면 그 값은 '펑' 터져버려요.
                # 터져버린 인형의 개수를 저장합니다.
                if len(bucket) > 1 and bucket[-1] == bucket[-2]:
                    del bucket[-2:]
                    answer += 2
                break
    return answer
