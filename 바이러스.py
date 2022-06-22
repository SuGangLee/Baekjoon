V = int(input())
E = int(input())

parent = [ i for i in range(V+1)]


def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

count=-1#1 자기자신 제외
for _ in range(E):
    a,b= map(int,input().split())
    union(parent,a,b)


for i in range(1,V+1): 
    if find_parent(parent,i)==1:
        count+=1
        
print(count)



