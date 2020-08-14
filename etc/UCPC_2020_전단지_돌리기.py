def distance(graph, s):
    cnt = 0
    cur = s
    tmp_value = []; tmp_cnt = []
    distance = []

    while True:
        if graph.get(cur):
            if len(graph.get(cur)) > 1:
                tmp_value.append(graph.get(cur))
                tmp_cnt.append(cnt)
            cur = graph.get(cur)[0]
            cnt += 1
            distance.append(cnt)

        elif tmp_value:
            for i in range(len(tmp_value)):
                cnt = tmp_cnt[i]
                for j in range(1, len(tmp_value[i])-1):
                    cur = graph.get(cur)[j]
                    cnt += 1
                del tmp_value[i]
                distance.append(cnt)

        else:
            for i in range(len(distance)):
                distance[i] = (distance[i]-1) * 2
            distance.sort(); distance.reverse()
            return distance[0]

graph = dict()
n, s, d = map(int, input().split())

for i in range(n): graph[i+1] = []
for i in range(n-1):
    t1, t2 = map(int, input().split())
    if graph.get(t1):
        graph[t1].append(t2)
    else:
        graph[t1] = [t2]

print(distance(graph, s))
