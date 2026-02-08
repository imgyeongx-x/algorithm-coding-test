year = int(input())

yoon = False

if year%4==0:
  yoon = True

if year%100==0:
  yoon = False

if year%400==0:
  yoon = True

if yoon == True:
  print(1)

else:
  print(0)