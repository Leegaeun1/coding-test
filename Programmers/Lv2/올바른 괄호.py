def solution(s):
    li=[] #스택
    for i in s:
        if i=='(': #열린 괄호일때 스택에 추가
            li.append(i)
        elif i==')': #닫히는 괄호일때 스택이 0이면 오류
            if len(li)==0:
                return False
            if li[-1]=='(': #맨마지막값이 열리는괄호면 추출
                li.pop()
            else: #아니면 오류
                return False
    if len(li)!=0: #다 끝났는데도 스택이 비어있지않으면 오류
        return False
    return True