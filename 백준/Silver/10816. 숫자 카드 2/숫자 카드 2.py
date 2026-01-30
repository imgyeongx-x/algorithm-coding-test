import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

from bisect import bisect_left, bisect_right

N = int(input())
card = list(map(int, input().split()))

M = int(input())
numList = list(map(int, input().split()))

card.sort()

def binary_search(num, start, end):
  global card

  if start > end: # 찾는 숫자가 존재하지 않음
    return 0
  
  mid = (start + end) // 2

  if card[mid] == num:
    # return card.count(card[mid])
    return bisect_right(card, card[mid]) - bisect_left(card, card[mid])
  
  elif card[mid] > num:
    end = mid-1
  else:
    start = mid+1
  
  mid = (start+end)//2
  return binary_search(num, start, end)


for i in range(M):
  print(binary_search(numList[i], 0, N-1), end=" ")