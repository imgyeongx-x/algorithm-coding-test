def gcd(a, b):
    while a % b != 0:
        tmp = a%b
        a = b
        b = tmp
    return b
        
def solution(arr):
    
    answer = 0
    
    n = arr[0]
    
    for i in range(1, len(arr)):
        n = (n * arr[i] / gcd(n, arr[i]))
    
    answer = n
    return answer