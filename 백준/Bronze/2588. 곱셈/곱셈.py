N = int(input())
M = int(input())
m = M

print(N * (m%10))
m = m // 10
print(N * (m%10))
m = m//10
print(N * (m%10))

print(N*M)