def combi(m,n):
    mul=1
    div=1
    for a in range(n):
        mul*=(m-a)
        div*=(n-a)
    return mul//div
def solution(n):
    cnt=0
    ma=n
    while(n>=0):
        cnt+=combi(ma,n)
        ma-=1 
        n-=2
    return cnt%1234567