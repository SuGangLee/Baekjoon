R,C = map(int,input().split())
# 열 행 
graph = [ list(input()) for _ in range(R) ]
result = 0
end_line = C-1
"""
def dfs(graph,y,x):
    if not 0<= x < C or not 0<= y < R :
        return False

    graph[y][x] =='x'
    if x == end_line:
        return True
    
    for dy,dx in ([1,1],[0,1],[-1,1]):
        nx = x+dx
        ny= y+dy
        if 0<= nx < C and 0<= ny < R and graph[ny][nx]=='.':
                    if dfs(graph,ny,nx):
                     return True
    return False   
   

#0부터 시작해서 한 칸씩 옮겨가므로 x 위치는 0으로 고정 
for y in range(R):
    if dfs(graph,y,0)==True:
                result+=1
                
    
print(result)"""

def go(x, y):
    graph[x][y] = 'x'
    if y == C - 1: return 1
    for nx in [x-1, x, x+1]:
        if 0 <= nx < R and graph[nx][y+1] == '.': 
            if go(nx, y+1): return 1
    return 0

print(sum(go(i, 0) for i in range(R)))
