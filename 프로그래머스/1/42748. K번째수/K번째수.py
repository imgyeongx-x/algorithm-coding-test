def solution(array, commands):
    answer = []
    
    for com in commands:
        arr1 = sorted(array[com[0]-1:(com[1])])
        answer.append(arr1[(com[2]-1)])
    
    return answer