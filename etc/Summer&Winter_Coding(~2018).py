def solution(skill, skill_trees):
    answer = 0

    # skill_trees 원소를 비교하기 위해서 반복문을 사용, 각 유저의 스킬트리(tree)
    # 일치하는 매칭값(mat), 스킬트리에 포함되는 스킬 개수(tot), 비교하는 원소 값을 나누기 위한 기준값(tmp)
    for tree in skill_trees:
        mat = 0; tot = 0; tmp = 0

        #mat, tmp = [mat+1, tree.find(i) for i in skill if i in tree[tmp:]]
        # 각 유저들의 스킬트리(tree)를 선행스킬(skill)에 적합한지 비교
        for i in skill:
            tot += tree.count(i)

            # 스킬트리는 선행스킬의 순서대로 진행되어야한다.
            if i == skill[0] or mat >= 1 and mat == skill.find(i):
                if i in tree[tmp:]:
                    tmp = tree.find(i)
                    mat += 1

        # 스킬트리가 선행스킬 조건을 고려했다면 mat과 tot변수가 일치해야 합니다.
        if mat == tot:
                answer += 1

    return answer
