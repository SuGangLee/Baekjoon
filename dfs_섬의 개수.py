import sys
sys.setrecursionlimit(10**7)
#상하좌우 대각선    
def dfs(x,y,graph,w,h):
    if 0 <= x < h and 0<= y < w:
        if graph[x][y] == 1:
                graph[x][y] = 0 #방문처리
                for dx,dy in ([-1,-1],[-1,0],[-1,1],[0, -1], [0, 1], [1, -1], [1, 0], [1, 1]):
                    nx = x+dx
                    ny= y+dy
                    dfs(nx,ny,graph,w,h)
                return True  #1이 연결된 부분 탐색완료     
        return False          
    return False
   
while 1:
    w,h = map(int,input().split())
    if w== h==0:
        break
    graph = [ list(map(int,input().split())) for _ in range(h)]
    result =0

    for i in range(h):
        for j in range(w):
            if dfs(i,j,graph,w,h)==True:
                result+=1
    print(result)


