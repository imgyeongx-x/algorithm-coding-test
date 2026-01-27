import sys
input = sys.stdin.readline

K = int(input())
stack = []


for i in range(K):
  num = int(input())
  if num == 0:
    if len(stack) != 0:
      stack.pop()
  else:
    stack.append(num)

print(sum(stack))