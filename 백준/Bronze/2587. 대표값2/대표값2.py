li = []

for i in range(5):
  n = int(input())
  li.append(n)

li.sort()

print(sum(li)//5)
print(li[2])