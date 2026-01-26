import sys
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

M = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
  left = 0
  right = N-1

  while left <= right:
    mid = (left + right) // 2
    if i > arr1[mid]:
      left = mid + 1
    elif i < arr1[mid]:
      right = mid - 1
    else:
      left = mid
      right = mid
      break

  if left == mid and right == mid:
    print(1)
  else:
    print(0)