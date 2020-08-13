def dfs(graph, start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        print(stack, graph[node])
        if node not in visited:
            visited.append(node)
            stack += graph[node]
    return visited

graph = dict()
n, s, d = map(int, input('숫자 3개 입력: ').split())

for i in range(n): graph[i+1] = []
for i in range(n-1):
    t1, t2 = map(int, input().split())
    if graph.get(t1):
        graph[t1].append(t2)
    else:
        graph[t1] = [t2]

#graph = dict()
#graph[1] = [2]; graph[2] = [3,4]; graph[3] = [5]; graph[4] = []; graph[5] = [6]; graph[6] = []
#print(dfs(graph, 1))


'''
from collections import deque

def DFS(graph, root):
    visited = []
    stack = [root]

    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
            if n in graph:
                temp = list(set(graph[n]) - set(visited))
                temp.sort(reverse=True)
                stack += temp
    return " ".join(str(i) for i in visited)

graph = {}
n, s, d = map(int, input('숫자 3개 입력: ').split())

for i in range(edge):
    edge_info = input().split(' ')
    n1, n2 = [int(j) for j in edge_info]
    if n1 not in graph:
        graph[n1] = [n2]
    elif n2 not in graph[n1]:
        graph[n1].append(n2)

    if n2 not in graph:
        graph[n2] = [n1]
    elif n1 not in graph[n2]:
        graph[n2].append(n1)

print(DFS(graph, start))
'''

'''
거리는 나중에 출력하고(+1을 해나가야겠지)

현재 노드에서 거리가 D 이하인 모든 노드에 전단지를 돌릴 수 있다는게 뭔 개소리지
D는 힘인데 힘이 1이면 1번 밖에 안되는게 아니야?


어떤 결과를 원하는가?
거리를 출력해야한다. 거리는 이동할 때마다 +1

이동은 어디로하나?
현민이가 목적을 달성하기위한 최소 거리를 향해.

목적은 무엇인가?
케니소프트에서 출발해 모든 노드에 전단지를 돌리고 돌아오는 것
(거리가 D 이하인 모든 노드에 전단지를 돌릴 수 있다)


현재 노드에서 갈 수 있는 가장 깊은 곳의 깊이 - 현재 노드의 깊이 >= D

가장 깊은 곳의 깊이는 어떻게 구하지?

1 2
2 3
2 4
3 5
5 6
현재 위치가 1이니까 1이 먼저인 것
1 2면 다음으로 2가 먼저인 것
2 3, 2 4가 있는데 둘 중 길이가 긴 것
3 5가 있다
5 6까지 있다
6까지 있으니 5까지만 이동하고 돌아온다?
카운트는 5까지만 하고 곱하기 2

DFS(깊이 우선 탐색 Depth First Search)

graph = dict()
graph[1] = [2,3]; graph[2] = [1,4]; graph[3] = [7,8,9]; graph[4] = [2,5,6]; graph[5] = [4]; graph[6] = [4]; graph[7] = [3]; graph[8] = [3]; graph[9] = [3,10]; graph[10] = [9]

def dfs(graph, start_node):
    visited, need_visit = list(), list()
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

print(dfs(graph, 1))
'''
