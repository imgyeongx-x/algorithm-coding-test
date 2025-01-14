n = int(input())

cnt = 0
isgroup = True

for i in range(0, n):
    text = input()
    li = []
    isgroup = True
    same = 0

    j = 0

    while j < len(text):
        same = 0
        for k in range(0, len(li)):
            if text[j] == li[k]:
                isgroup = False
                break
        if isgroup == False:
            break
        li.append(text[j])
        for k in range(j + 1, len(text)):
            if text[j] == text[k]:
                same+=1
            else:
                break
        if same == 0:
            j += 1
        else:
            j = j + same + 1
    if isgroup == True:
        cnt+=1

print(cnt)