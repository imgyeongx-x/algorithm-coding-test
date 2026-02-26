st = [0] * 5

for i in range(5):
    tmp = int(input())
    if tmp < 40:
        tmp = 40
    st[i] = tmp

print(int(sum(st)//5))