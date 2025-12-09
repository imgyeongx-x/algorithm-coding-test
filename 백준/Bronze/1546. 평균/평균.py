N = input()
scores = list(map(int, input().split()))

bestScore = max(scores)
sum = sum(scores)

print(sum / bestScore * 100 / int(N))