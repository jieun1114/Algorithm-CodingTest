# 동전 0 - solved
import sys

n, k = map(int,sys.stdin.readline().split())
coin = []

for i in range(n):
    coin.append(int(sys.stdin.readline().strip()))

coin.reverse()

cnt = 0

for won in coin:
    if won <= k:
        cnt += k//won
        k = k%won

    if k == 0:
        break

print(cnt)