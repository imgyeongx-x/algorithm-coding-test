n = int(input())
n0 = 0
n1 = 1
n2 = 0

for i in range(2, n+1):
  n2 = n0 + n1
  n0 = n1
  n1 = n2


if n == 0:
  print(0)
elif n == 1:
  print(1)
else:
  print(n2)
