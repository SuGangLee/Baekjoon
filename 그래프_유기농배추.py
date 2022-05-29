import sys
sys.setrecursionlimit(10**7) # 재귀 한도 늘려줌
# 이코테의 dfs 4번 호출 하는 식으로는 런타임 에러 뜸 -> 아니다! w,h,N 을 T 만큼 입력받는거 까먹고 한번 씩 받음@!

def dfs(y,x,w,h,graph):
    if  0 <= x < w and 0 <= y < h:   
        if graph[y][x] == 1:
                graph[y][x] = 0 
                for dy,dx in ([-1,0],[0, -1], [0, 1], [1, 0]):                   
                    ny= y+dy     
                    nx = x+dx 
                    dfs(ny,nx,w,h,graph)
                return True
        return False
    return False 

T =int(input())


for t in range(T):
    result = 0 
    w,h,N = map(int,input().split())
    graph = [ [0]*(w) for _ in range(h)]
    
    for i in range(N):
        dx,dy = map(int,input().split())
        graph[dy][dx]=1
   
    for i in range(h):
        for j in range(w):
            if dfs(i,j,w,h,graph) == True:
                result+=1
    print(result)