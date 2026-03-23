month, day = map(int, input().split())
li = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = day
for i in range(1, month):
  total += li[i]

Dow = (total % 7)

if Dow == 1:
  print("MON")
elif Dow == 2:
  print("TUE")
elif Dow == 3:
  print("WED")
elif Dow == 4:
  print("THU")
elif Dow == 5:
  print("FRI")
elif Dow == 6:
  print("SAT")
elif Dow == 0:
  print("SUN")