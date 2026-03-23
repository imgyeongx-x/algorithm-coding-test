n = int(input())

for i in range(0, n-1):
  for j in range(0, n-i-1):
    print(" ", end="")
  for j in range(0, i):
    if j == 0:
      print("*", end="")
    else:
      print(" ", end="")
    print(" ", end="")
  print("*", end="")
  print()
for i in range(2*n-1):
  print("*", end="")