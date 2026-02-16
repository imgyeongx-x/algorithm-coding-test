import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
  tmp = input().split()
  cmd = tmp[0]

  if cmd != "all" and cmd != "empty":
    num = int(tmp[1])

  if cmd == "add":
    if not num in S:
      S.add(num)
  elif cmd == "remove":
    if num in S:
      S.remove(num)
  elif cmd == "check":
    if num in S:
      print(1)
    else:
      print(0)
  elif cmd == "toggle":
    if num in S:
      S.remove(num)
    else:
      S.add(num)
  elif cmd == "all":
    S = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
  elif cmd == "empty":
    S.clear()