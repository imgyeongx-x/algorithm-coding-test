N = int(input())

li = list(map(int, input().split()))
lis = [float("-inf")]
total = []

for i in range(0, N):
  if lis[-1] < li[i]:
    lis.append(li[i])
    total.append([li[i], len(lis)-1])
  else:
    st = 0
    ed = len(lis)
    while (st < ed):
      mid = (st + ed) // 2
      if lis[mid] < li[i]:
        st = mid+1
      else:
        ed = mid
    lis[ed] = li[i]
    total.append([li[i], ed])

res = [0] * (len(lis)-1)
index = len(lis) - 1

for i in range(N-1, -1, -1):
  if index == total[i][1]:
    res[total[i][1]-1] = total[i][0]
    index -= 1
    
print(len(res))

for i in res:
  print(i, end=" ")