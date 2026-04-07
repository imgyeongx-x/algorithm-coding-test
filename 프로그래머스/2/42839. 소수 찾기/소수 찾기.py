from itertools import permutations

def solution(numbers):
    answer = 0
    answerList = []
    isPrime = [True] * 10000002
    isPrime[0] = False
    isPrime[1] = False
    
    for i in range(2, 10000000):
        if isPrime[i] == True:
            for j in range(i*2, 10000000, i):
                isPrime[j] = False
                
    li = list(numbers)
    for i in range(len(li)):
        n = int(li[i])
        if isPrime[n] == True:
            answerList.append(n)
    
    for i in range(2, len(li)+1):
        tmp = list(permutations(numbers, i))
        for j in tmp:
            n = ''
            for k in j:
                n+=k
            num = int(n)
            if isPrime[num] == True:
                answerList.append(num)
                
    answerList = set(answerList)
    
    return len(answerList)