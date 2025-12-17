import sys

input = sys.stdin.readline

li = [0] * 3

while True:
  li[0], li[1], li[2] = map(int, input().split())
  if li[0] == 0 and li[1] == 0 and li[2] == 0:
    break
  li.sort()
  if li[2] >= li[0] + li[1]:
    print("Invalid")
  elif li[0] == li[1] == li[2]:
    print("Equilateral")
  elif li[0] == li[1] or li[1] == li[2]:
    print("Isosceles")
  else:
    print("Scalene")