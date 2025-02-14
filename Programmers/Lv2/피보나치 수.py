def solution(n):
    li=[0,1]
    for a in range(n-1):
        f=li[0]
        s=li[1]
        li[0]=s
        li[1]=f+s
    return li[1]%1234567