N = int(input())

arr = [-1] * 5001

arr[3] = 1
arr[5] = 1

for i in range(6, N+1):
  if arr[i-3] != -1 and arr[i-5] != -1:
    arr[i] = min(arr[i-3], arr[i-5]) + 1
  elif arr[i-3] != -1:
    arr[i] = arr[i-3] + 1
  elif arr[i-5] != -1:
    arr[i] = arr[i-5] + 1

print(arr[N])