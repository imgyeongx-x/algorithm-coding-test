from bisect import bisect_left

N = int(input())

arr = sorted(list(map(int, input().split())))

answer = 0

for i in range(len(arr)-2):
  start, end = i+1, N-1

  while start < end:
    result = arr[i] + arr[start] + arr[end]
    if result > 0:
      end -= 1
    else:
      if result == 0:
        if arr[start] == arr[end]:
          answer += end-start
        else: 
          answer += (end - bisect_left(arr, arr[end]) + 1)
      start += 1

print(answer)