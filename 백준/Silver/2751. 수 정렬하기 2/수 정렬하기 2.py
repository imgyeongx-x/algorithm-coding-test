import sys
input = sys.stdin.readline

N = int(input())
li = [0] * N

for i in range(N):
  li[i] = int(input())

li.sort()

for i in range(N):
  print(li[i])