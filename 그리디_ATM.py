k = int(input())
p = list(map(int,input().split()))
result=0

p=sorted(p)

for i in range(k):
    for j in range(0,i+1):
        result += p[j]

print(result)       

