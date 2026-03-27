import heapq
import sys
input = sys.stdin.readline

N = int(input())
leftHeap = [] #중간값보다 작은 값 / 중간 값은 leftHeap[0]
rightHeap = [] # 중간값보다 큰 값

for i in range(N):
  num = int(input())
  if len(leftHeap) == 0 and len(rightHeap) == 0:
    heapq.heappush(leftHeap, -num)
  
  else:
    if len(rightHeap) == len(leftHeap):
      heapq.heappush(leftHeap, -num)
    else:
      heapq.heappush(rightHeap, num)

    if len(rightHeap) != 0 and rightHeap[0] < (-leftHeap[0]):
      leftValue = -heapq.heappop(leftHeap)
      rightValue = heapq.heappop(rightHeap)

      heapq.heappush(leftHeap, -rightValue)
      heapq.heappush(rightHeap, leftValue)

  print(-leftHeap[0])