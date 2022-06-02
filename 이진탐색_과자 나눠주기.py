import sys

M,N = map(int,sys.stdin.readline().split())

snack =list(map(int,sys.stdin.readline().split()) )
result = 0
start = 0
end = max(snack)

while start <= end:
    mid = (start+end) // 2
    sum = 0
    if mid == 0: #모든 조카 줄 수 없는 경우 
        result = 0
        break   
    
    for i in snack:
        sum+= i // mid 
    
    if sum >=  M:   # 중간 값보다 긴 과자가 M개 이상? => 모든 조카 주기 가능?     
        start = mid+1 
        result = mid #결과 저장, 조카들 줄 과자 길이, mid가 0일 때 고려해야하므로 End가 출력이 될 수 없어

    else :
        end = mid -1 

    

print(result)
