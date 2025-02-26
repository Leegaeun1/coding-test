def trans(n):
    st=''
    while(n>0):
        if n%3==0:
            st='4'+st
            n=n//3-1
        else:
            st=str(n%3)+st
            n//=3
    return st

def solution(n):
    answer = trans(n)
    return answer