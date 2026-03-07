# 백준 1931번
# 회의실 배정

N = int(input())
endPoint = 0
answer = 0
meeting = []

for i in range(N):
  li = list(map(int, input().split()))
  meeting.append(li)

meeting.sort(key=lambda x: (x[1], x[0]))

for st, ed in meeting:
  if endPoint <= st:
    answer += 1
    endPoint = ed

print(answer)