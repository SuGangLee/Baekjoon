n,k = map(int,input().split())
Ai= [int(input()) for _ in range(n)]

count=0
for i in reversed(range(n)): #reversed 사용 시 i : n-1,n-2 ---- 0     
    if Ai[i] < k:
        count+= k//Ai[i]
        k=k%Ai[i]
        
    
print(count)