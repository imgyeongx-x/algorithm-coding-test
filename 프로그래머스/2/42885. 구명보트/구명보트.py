def solution(people, limit):
    answer = 0
    left = 0
    right = len(people) - 1
    
    people.sort()
    
    while left <= right:
        if left == right:
            answer += 1
            break
        if people[left] + people[right] <= limit:
            answer += 1
            left += 1
            right -= 1
        else:
            answer += 1
            right -= 1
    
    return answer