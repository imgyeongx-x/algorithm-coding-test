N, M = map(int, input().split())

not_listen = set()
not_all = set()

for i in range(N):
  tmp = input()
  not_listen.add(tmp)

for i in range(M):
  tmp = input()
  if tmp in not_listen:
    not_all.add(tmp)

not_all=sorted(not_all)

print(len(not_all))
for i in not_all:
  print(i)