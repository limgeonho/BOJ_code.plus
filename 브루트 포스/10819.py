# 차이를 최대로
from itertools import permutations
n = int(input())
array = list(map(int, input().split()))

new_array = list(permutations(array, n))
total = 0
for arr in new_array:
    tmp = 0
    for i in range(len(arr)-1):
        tmp += abs(arr[i] - arr[i+1])
    total = max(total, tmp)
print(total)