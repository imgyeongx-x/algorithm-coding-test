import sys
input = sys.stdin.readline

K, N = map(int, input().split())

arr = [0] * K

for i in range(K):
  arr[i] = int(input())

max = max(arr)

start = 1
end = max

while (start <= end):
  middle = (start + end) // 2
  cnt = 0
  for i in range(K):
    cnt += arr[i] // middle

  if cnt < N:
    end = middle - 1
  else:
    start = middle + 1
    
print(end)