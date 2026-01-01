import sys

input = sys.stdin.readline

N = int(input())
st = list(map(int, input().split()))

ans = [-1] * N
myStack = []
top = -1

for i in range(N):
  while top != -1 and st[i] > st[myStack[top]]:
    ans[myStack[top]] = st[i]
    top -= 1
    myStack.pop()      
  myStack.append(i)
  top+=1

for i in range(N):
  sys.stdout.write(str(ans[i]) + " ")