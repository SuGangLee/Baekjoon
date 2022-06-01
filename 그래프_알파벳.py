#시간초과되는 코드
import sys

h,w = map(int,sys.stdin.readline().split())
board = [ list(sys.stdin.readline()) for _ in range(h) ]
visited_alpha = set()

ans =0 

def dfs(y,x,count):
    global ans
    ans = max(ans,count)
    for dy,dx in ([-1,0],[0, -1], [0, 1], [1, 0]): 
        ny= y+dy     
        nx = x+dx    
        if 0<= nx < w and 0<=ny<h:
            if board[ny][nx] not in visited_alpha:
                visited_alpha.add(board[ny][nx])                         
                dfs(ny,nx,count+1)
                visited_alpha.remove(board[ny][nx])
                
visited_alpha.add(board[0][0])
dfs(0,0,1) 
print(ans)

