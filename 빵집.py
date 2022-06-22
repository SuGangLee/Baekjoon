R,C = map(int,input().split())
# 열 행 
graph = [ list(input()) for _ in range(R) ]

result=0
def go(x, y):
    graph[x][y] = 'x'
    if y == C - 1: return True

    for nx in [x-1, x, x+1]:
        if 0 <= nx < R and graph[nx][y+1] == '.': 
            if go(nx, y+1): 
                return True
    return False

for i in range(R):
    if go(i,0):
        result+=1

print(result)
