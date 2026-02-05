N = int(input())
arr = [0] * N

for i in range(N):
  arr[i] = int(input())

res = 0
for i in range(N-2, -1, -1):
  if arr[i+1] <= arr[i]:
    res += arr[i] - arr[i+1] + 1
    arr[i] = arr[i+1]-1

print(res)