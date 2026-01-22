import sys
input = sys.stdin.readline

N, sumN = map(int, input().split())
arr = list(map(int, input().split(" ")))

i = 0
j = 1
cnt = 0

while i <= j and j <= N:
  total = sum(arr[i:j])

  if total < sumN:
    j += 1
  elif total > sumN:
    i+=1
  else:
    cnt += 1
    j += 1

print(cnt)