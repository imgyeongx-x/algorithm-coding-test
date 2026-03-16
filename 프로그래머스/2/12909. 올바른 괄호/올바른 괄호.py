from collections import deque
def solution(s):
    answer = True
    
    st = deque()
    for i in s:
        if i == '(':
            st.append('(')
        if i == ')':
            if len(st) != 0:
                st.pop()
            else:
                answer = False
    if len(st) != 0 and answer == True:
        answer = False

    return answer