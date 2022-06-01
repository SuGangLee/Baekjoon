import heapq
import sys
N = int(input())

heap = []
for i in range(N):
    x = int(sys.stdin.readline()) #input()으로 할 시 시간초과
    if x == 0 :
        if not heap  :
            print(0)
        else : 
            print(heapq.heappop(heap))

    else: 
        heapq.heappush(heap,x)