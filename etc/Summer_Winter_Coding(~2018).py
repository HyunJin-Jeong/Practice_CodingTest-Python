def solution(skill, skill_trees):
    answer = 0

    for tree in skill_trees:
        count = 0
        tmp = 0

        for i in skill:
            if i in tree[tmp:]:
                tmp = tree.find(i)
                count += 1

        if count == len(skill):
            answer += 1

    return answer
    
print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))
