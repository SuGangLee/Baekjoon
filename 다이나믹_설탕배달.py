from cmath import inf


N = int(input())

 
d = [10001]*(N+10)

d[3]=d[5]=1
for i in range(6,N+1):
    if d[i-5]!=10001:
        d[i]=min(d[i],d[i-5]+1)
    if d[i-3]!=10001:
        d[i]=min(d[i],d[i-3]+1)

if d[N]==10001:
    print(-1)
else:
    print(d[N])
