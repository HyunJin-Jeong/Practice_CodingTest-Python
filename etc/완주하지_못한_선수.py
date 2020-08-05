import copy
def solution(participant, completion):
    completion.sort(); participant.sort();
    for i in completion:
        participant.remove(i)
    return ''.join(participant)

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
