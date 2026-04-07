def solution(sizes):
    answer = 0
    wallet = [0,0]
    
    for i in range(len(sizes)):
        s = sorted(sizes[i])
        if wallet[0] < s[0]:
            wallet[0] = s[0]
        if wallet[1] < s[1]:
            wallet[1] = s[1]
    
    return wallet[0] * wallet[1]