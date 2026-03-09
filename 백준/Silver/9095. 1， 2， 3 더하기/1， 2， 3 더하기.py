import sys
input = sys.stdin.readline

N = int(input())
arr = [0] * N

for i in range(N):
  arr[i] = int(input())

sumArr = [0] * (11)

sumArr[1] = 1
sumArr[2] = 2
sumArr[3] = 4

for i in range(4, 11):
  sumArr[i] = sumArr[i-1] + sumArr[i-2] + sumArr[i-3]

for i in range(N):
  num = arr[i]
  print(sumArr[num])