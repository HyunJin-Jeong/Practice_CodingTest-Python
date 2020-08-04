import copy

def solution(participant, completion):

    answer = copy.deepcopy(participant)

    for i in participant:
        if i in completion:
            answer.remove(i); completion.remove(i)

    return ''.join(answer)

    #return [answer.remove(i), completion.remove(i) for i in participant if i in completion]

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
