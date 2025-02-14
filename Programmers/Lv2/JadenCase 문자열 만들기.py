def solution(s):
    s=list(s) #리스트로 변환
    cnt=0 #공백인지 걸러주는 용도
    for i in range(len(s)):
        if s[i]!=" ": #공백이 아니면 1증가
            cnt+=1
        else:
            cnt=0 #공백일때 0으로 초기화
        if cnt==1: #공백 바로 이후니까 대문자표현
            s[i]=s[i].upper()
        else:
            s[i]=s[i].lower()
    return "".join(s)