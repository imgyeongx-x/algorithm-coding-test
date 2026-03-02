# 백준 2748번 피보나치 수 2

# 풀이 알고리즘 : Dynamic Programming
# 점화식 : f(n) = f(n-1) + f(n-2)

N = int(input())

fibo = [0] * (N+1)

fibo[1] = 1

for i in range(2, N+1):
  fibo[i] = fibo[i-1] + fibo[i-2]

print(fibo[N])