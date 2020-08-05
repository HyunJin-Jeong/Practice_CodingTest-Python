import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return ''.join(answer.keys())

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
