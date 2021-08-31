# 다음 순열
from itertools import permutations

n = int(input())
to_find = tuple(map(int, input().split()))
array = tuple(range(1, n+1))
answer = list(permutations(array, n))
idx = answer.index(to_find)
if idx == len(answer)-1:
    print(-1)
else:
    print(*answer[idx+1])