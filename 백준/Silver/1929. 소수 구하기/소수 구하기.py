N, M = map(int, input().split())
li = [True] * (M+1)

for i in range(1, M+1):
  if i == 1:
    continue
  if li[i] == True:
    if N <= i:
      print(i)
    for j in range(i*2, M+1, i):
      li[j] = False