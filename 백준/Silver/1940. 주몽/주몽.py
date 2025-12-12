import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
arr = list(map(int, input().split()))

arr.sort()
st_index = 0
ed_index = N-1
cnt = 0

while (st_index < ed_index):
  if (arr[st_index] + arr[ed_index]) == M:
    st_index+=1
    ed_index-=1
    cnt+=1
  elif (arr[st_index] + arr[ed_index]) > M:
    ed_index-=1
  else:
    st_index+=1

print(cnt)