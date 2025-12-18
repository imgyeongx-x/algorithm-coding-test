N = int(input())

A = [0] * N

for i in range(N):
  A[i] = int(input())

st = []
num = 1
Result = True
answer = []

for i in range (N):
  su = A[i]
  if su >= num:
    while su >= num:
      st.append(num)
      num+=1
      answer.append("+")
    st.pop()
    answer.append("-")
  else:
    tmpop = st.pop()
    if tmpop > su:
      print("NO")
      Result = False
      break
    else:
      answer.append("-")

if Result == True:
  for i in answer:
    print(i)