from sys import stdin
_ = stdin.readline()
N = map(int,stdin.readline().split())
_ = stdin.readline()
M = map(int,stdin.readline().split())
#딕셔너리 자료형 사용 
hashmap = {}
for n in N:
    if n in hashmap:
        hashmap[n] += 1
    else:
        hashmap[n] = 1

print(' '.join(str(hashmap[m]) if m in hashmap else '0' for m in M))

from collections import Counter
#리스트 N을 Counter에 넣으면 N의 요소들의 숫자를 센 Dictionary자료형이 출력됩니다.
C = Counter(N)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M))
