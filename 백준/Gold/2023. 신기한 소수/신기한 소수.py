import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input())

def isPrime(a):
  for i in range(2, int(a**0.5) + 1):
    if a % i == 0:
      return False
  return True


def DFS(a):
  if len(str(a)) == N:
    print(a)
  else:
    for i in range(1, 10, 2):
      if isPrime(a * 10 + i):
        DFS(a * 10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)
