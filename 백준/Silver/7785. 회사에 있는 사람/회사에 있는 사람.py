import sys
input = sys.stdin.readline

N = int(input())

work = {}

for i in range(N):
  name, check = map(str, input().split())

  if name in work:
    work[name] = check
  else:
    work[name] = check

workList=[]
for i in work:
  if work[i] == "enter":
    workList.append(i)

workList.sort(reverse=True)

for i in workList:
  print(i)