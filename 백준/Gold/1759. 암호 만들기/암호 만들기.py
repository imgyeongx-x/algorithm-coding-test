import sys
input = sys.stdin.readline
from itertools import combinations

L, C = map(int, input().split())

arr = input().split()
arr.sort()

for i in combinations(arr, L):
  str = ''
  vowel = 0
  consonants = 0
  for j in i:
    if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u':
      vowel += 1
    else:
      consonants += 1
    str += j
  if vowel >= 1 and consonants >= 2:
    print(str)