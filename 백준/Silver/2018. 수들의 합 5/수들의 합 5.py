import sys

input = sys.stdin.readline

N = int(input())

cnt = 1

st_index = 1
en_index = 1
sumN = 1

while True:
  if st_index==N:
    break
  if sumN == N:
    cnt+=1
    en_index+=1
    sumN+=en_index
  elif sumN < N:
    en_index += 1
    sumN += en_index
  else:
    sumN -= st_index
    st_index += 1

print(cnt)