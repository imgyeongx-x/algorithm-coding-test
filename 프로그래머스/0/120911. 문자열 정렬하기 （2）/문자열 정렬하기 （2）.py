def solution(my_string):
    answer = ''
    for c in sorted(my_string.lower()):
        answer += c
    return answer