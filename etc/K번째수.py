def solution(array, commands):
    answer = []
    for a in commands:
        i = a[0]-1; j = a[1]; k = a[2]-1;
        answer.append(sorted(array[i:j])[k])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))
