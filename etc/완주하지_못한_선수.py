import copy
def solution(participant, completion):
    completion.sort(); participant.sort();
    for i in completion:
        participant.remove(i)
    return ''.join(participant)
