N = int(input())

arr = list(map(int, input().split()))

sortedList = sorted(list(set(arr)))

dict = {}

for i in range(len(sortedList)):
  dict[sortedList[i]] = i

for i in arr:
  print(dict[i], end=" ")