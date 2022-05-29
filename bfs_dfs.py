#dfs 

from collections import deque 

N,M,v = map(int,input().split())
graph=[[] for _ in range(N+1)]

for i in range(1,M+1):
    a,b= map(int,input().split())
    graph[a].append(b)

visited =[False]*(N+1)
visited_bfs =[False]*(N+1)

def dfs(graph,v,visited):
    visited[v] =True
    print(v,end=' ')
    for i in graph[v]:
        if visited[i] == False :
            dfs(graph,i,visited)

def bfs(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    
    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

dfs(graph,v,visited)
print()
bfs(graph,v,visited_bfs)
print()