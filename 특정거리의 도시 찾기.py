import sys
import heapq
N,M,K,x = map(int,sys.stdin.readline().split())
inf =1e9
graph = [ [] for _ in range(N+1)]

for i in range(M):
    a,b =  map(int,sys.stdin.readline().split())
    graph[a].append((b,1))

distance =[inf]*(N+1)

def find_distance (start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q: 
        dist,now= heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist+ i[1]
            if cost < distance[i[0]]:
                    distance[i[0]] = cost                
                    heapq.heappush(q,(cost,i[0]))
                    
       
find_distance(x)
isFind = False
for i in range(len(distance)):
    if distance[i] == K:
        isFind = True
        print(i)


if not isFind:
    print(-1)

    

    





