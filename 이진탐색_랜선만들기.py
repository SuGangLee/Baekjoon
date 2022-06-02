import sys

K,N = map(int,sys.stdin.readline().split() )
lan = [int(sys.stdin.readline()) for _ in range(K) ]

start = 1
end = max(lan)

while start <= end:
    mid = (start+end)//2
    sum=0   
    for i in lan:
        sum += i//(mid)
    
    if sum >= N:       
        start = mid+1
    else :
        end = mid -1
        

print (end) # 최대 랜선의 길이이므로 end 출력