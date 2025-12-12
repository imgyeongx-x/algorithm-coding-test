import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0

for K in range(N):
  i = 0
  j = N-1
  while (i < j):
    sumN = arr[i] + arr[j]
    if (sumN == arr[K]):
      if i == K:
        i+=1
      elif j == K:
        j-=1
      else:
        cnt+=1
        break
    elif (sumN > arr[K]):
      j-=1
    else:
      i+=1

print(cnt)