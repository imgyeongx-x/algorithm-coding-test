import sys

input = sys.stdin.readline

N = int(input())
maxW = [0] * N

for i in range(N):
  maxW[i] = int(input())

maxW.sort()
result = 0

for i in range(N):
  if result < maxW[i]*(N-i):
    result = maxW[i]*(N-i)

print(result)