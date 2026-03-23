s = input()

for i in range(0, len(s), 10):
  st = i
  ed = i+10
  if ed >= len(s):
    ed = len(s)
  print(s[st:ed])