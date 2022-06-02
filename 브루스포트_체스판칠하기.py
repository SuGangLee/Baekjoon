N,M = map(int,input().split())

chess = [ input() for _ in range(N)]
count = []

for a in range(N-7):
    for b in range(M-7):
        check1 = check2 = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i+j) % 2==0:
                    if chess[i][j]!='W':
                        check1 +=1
                    else:
                        check2 +=1
                else:
                    if chess[i][j]!='W':
                        check2+=1
                    else:
                        check1+=1
        count.append(min(check1,check2))

print(min(count))
