import copy

def solution(participant, completion):

    answer = copy.deepcopy(participant)
    [(answer.remove(i), completion.remove(i)) for i in participant if i in completion]
    return ''.join(answer)

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
