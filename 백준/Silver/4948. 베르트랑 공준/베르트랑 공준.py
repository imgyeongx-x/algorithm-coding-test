prime = [True] * 250000

for i in range(1, 250000):
  if i == 1:
    prime[i] = False
  if prime[i] == True:
    for j in range(i * 2, 250000, i):
      prime[j] = False


while True:
  N = int(input())
  if N == 0:
    break
  M = N * 2
  
  cnt = 0
  for i in range(N+1, M+1):
    if prime[i] == True:
      cnt += 1
  print(cnt)