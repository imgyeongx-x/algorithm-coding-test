import sys
sys.setrecursionlimit(100000)

input = sys.stdin.readline

M = [list(map(int, input().split())) for _ in range(10)]

S = [0, 5, 5, 5, 5, 5] # 색종이수 저장

# result = -1 -> 이 코드를 사용하지 않은 이유는, M이 전부 0일 때를 반영하지 못하기 때문이다.
# 왜냐하면, used가 0이라면 result -1보다 큰것이라서, -1이 유지된다.
# 따라서, result를 양의 무한대로 설정한다.
result = float('inf') # float('inf') 는 양의 무한대를 의미함

def fill(x, y, size, value):
  for i in range(y, y+size):
    for j in range(x, x+size):
      M[i][j] = value

def can_attatch(x, y, size):
  if x + size > 10 or y + size > 10:
    return False
  for i in range(y, y+size):
    for j in range(x, x+size):
      if M[i][j] != 1:
        return False
  return True

## 초기 생각
#def backTrack(posx, posy, used):
#  global result
#  if posx == 10 and posy == 10:
#    result = min(result, used)
#    return
#  if used >= result:
#    return
#  
#  if M[posx][posy] == 1:
#    for size in range(5, 0, -1): # #5에서부터 1까지의 색종이 탐색
#      if S[size] > 0 and can_attatch#(posx, posy, size):
#        S[size] -= 1
#        fill(posx, posy, size, 0)
#        #backTrack(posx + 1, posy + 1, #used + 1)

def backTrack(pos, used):
  global result
  if pos == 100:
    result = min(result, used)
    return
  if used >= result:
    return

  x, y = divmod(pos, 10)
  # divmod : 몫과 나머지를 동시에 구하는 함수
  # 현재 상황에서, x와 y의 위치를 구하는 것에 도움이 됨 

  if M[y][x] == 1:
    for size in range(5, 0, -1): # 5에서부터 1까지의 색종이 탐색
      if S[size] > 0 and can_attatch(x, y, size):
        S[size] -= 1
        fill(x, y, size, 0)
        backTrack(pos + 1, used + 1)
        # 위 backTrack을 위해 divmod로 x,y 좌표로 값을 구하는 것 !
        # 만약 posx, posy로 한다면 posx 가 10이면 posy를 +1하고 posx를 0으로 하는 등
        # divmod로 x,y를 구하는 것 보다 복잡하게 생각해야한다.
        # x, y = divmod(pos, 10) 는 컴팩트하게 backTrack을 진행할 수 있게 해주는 구문

        fill(x, y, size, 1)
        # fill에 value가 있는 이유.
        # backTrack이 끝나고 0으로 덮었던 숫자들을 다시 1로 원복해야함

        S[size] += 1

  else:
    backTrack(pos + 1, used)

backTrack(0, 0) # pos = 0, used = 0

# print(result)
# result가 변경되었다면 해당 숫자, 아니라면 기본으로 설정했던 -1이 print될 것이라고 생각했으나,
# 전체가 0으로 입력된 M에서 오류가 발생함

print(result if result != float('inf') else -1)