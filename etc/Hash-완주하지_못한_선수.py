def solution(participant, completion):
    answer = []
    answer += [i for i in participant if i not in completion]
    return answer

print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
