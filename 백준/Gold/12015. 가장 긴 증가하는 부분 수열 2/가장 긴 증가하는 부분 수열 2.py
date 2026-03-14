import sys
input = sys.stdin.readline

N = int(input())
li = list(map(int, input().split()))

bs = []
bs.append(0)
bs.append(li[0])

for i in range(1, N):
  if bs[-1] < li[i]:
    bs.append(li[i])
  else:
    st = 0
    ed = len(bs)
    while (st < ed):
      mid = (st+ed)//2
      if bs[mid] < li[i]:
        st = mid + 1
      else:
        ed = mid
    bs[ed] = li[i]
  
print(len(bs)-1)