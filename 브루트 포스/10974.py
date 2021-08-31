# 모든 순열
from itertools import permutations

n = int(input())
array = list(range(1, n+1))

for perm in permutations(array, n):
    print(*perm)