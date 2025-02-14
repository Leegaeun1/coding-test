def solution(s): 
    li=[] #스택
    for a in range(len(s)):
        li.append(s[a]) #스택에 추가
        if len(li)>1: # 스택에 2개이상일때
            if li[-2]==li[-1]: #자신의 전 값이랑 같으면
                li.pop() #전 값과 자신 삭제하기
                li.pop()
    if len(li)==0: #길이 0이면 1리턴
        return 1
    return 0