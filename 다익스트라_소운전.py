import sys
import heapq

INF = (1e9)
V,E = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(E)]
distance = [INF] * (V+1)

for i in range(E):
    x,y,time,taste = map(int,sys.stdin.readline().split())
    graph[x].append((y,time,taste))

print(graph)


def shortPath(start):
    q=[]
    heapq.heappush(q,(0,0,start))
    distance[start] = 0
    # -- 기본 값 초기화 
    while q:
        print(q)
        dist,food,now_node = heapq.heappop(q)
        if distance[now_node] < dist:
            continue
        for i in graph[now_node]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance [i[0]] = cost                      
                heapq.heappush(q,(cost,i[2],i[0]))

shortPath(1)
for i in range(2,V+1):
        print (distance[i])


