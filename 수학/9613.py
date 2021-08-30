# GCD합
from math import gcd
from itertools import combinations

T = int(input())

for _ in range(T):
    array = list(map(int, input().split()))
    tmp = list(combinations(array[1:], 2))
    # print(tmp)
    total = 0
    for i in tmp:
        total += gcd(i[0], i[1])
    print(total)
