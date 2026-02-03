import sys
input = sys.stdin.readline

N = int(input())
card = list(map(int, input().split()))

M = int(input())
check = list(map(int, input().split()))

card.sort()

def find_card(num):
  start = 0
  end = N-1

  while (start <= end):
    middle = (start+end)//2
    if card[middle] == num:
      return 1
    elif card[middle] > num:
      end = middle - 1
    else:
      start = middle + 1
  
  return 0

for i in range(M):
  print(find_card(check[i]), end=" ")