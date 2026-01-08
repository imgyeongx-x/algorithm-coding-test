import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split(" ")))

P.sort()

S = [0] * N

S[0] = P[0]

for i in range(1, N):
  S[i] = S[i-1] + P[i]

print(sum(S))