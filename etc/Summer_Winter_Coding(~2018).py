def solution(skill, skill_trees):
    answer = 0
    answer = ["hi" for i in skill_trees if skill in i]

    '''
    for i in skill_trees:
        if skill in i:
            answer += 1
    '''
    return answer


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
