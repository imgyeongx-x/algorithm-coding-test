def solution(answers):
    answer = []
    s1 = [1,2,3,4,5]
    s2 = [2,1,2,3,2,4,2,5]
    s3 = [3,3,1,1,2,2,4,4,5,5]
    a1, a2, a3 = 0, 0, 0
    for i in range(len(answers)):
        if answers[i] == s1[i%len(s1)]:
            a1 += 1
        if answers[i] == s2[i%len(s2)]:
            a2 += 1
        if answers[i] == s3[i%len(s3)]:
            a3 += 1
    
    am = max(a1, a2, a3)
    if a1 == am:
        answer.append(1)
    if a2 == am:
        answer.append(2)
    if a3 == am:
        answer.append(3)
        
    return answer