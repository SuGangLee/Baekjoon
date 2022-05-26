
from cmath import inf
import sys

read = sys.stdin.readline
N = int(read())

d = [inf] * (N+1) #무한대로 초기화!! min 값으로 비교해서 넣기 때문에
d[3] = d[5] = 1

for i in range(6, N):
    d[i] = min(d[i-3], d[i-5]) + 1 #3과 5를 뺐을 때 구할 수 있는 수 중 더 작은 값

print(d[N] if d[N] < inf  else -1)
