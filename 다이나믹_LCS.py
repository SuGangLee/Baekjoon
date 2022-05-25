s1= input()
s2=input()
d = [0]*(len(s2))
for i in range(len(s1)):
    count=0
    for j in range(len(s2)):
        if count < d[j]:
            count = d[j]
        elif s1[i] == s2[j]:
            d[j]=count+1
print(max(d))