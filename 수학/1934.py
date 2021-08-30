# 최소공배수
from math import gcd

T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    print(int(n * m / gcd(n, m)))
