from queue import PriorityQueue

que = PriorityQueue()

N = int(input())
for i in range(N):
  num = int(input())
  que.put(num)

num1 = 0
num2 = 0
sum1 = 0

while que.qsize() > 1:
  num1 = que.get()
  num2 = que.get()
  temp = num1 + num2
  sum1 += temp
  que.put(temp)

print(sum1)