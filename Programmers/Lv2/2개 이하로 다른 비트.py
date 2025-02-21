def binary(n):
    st=''
    while(n>0):
        st+=str(n%2)
        n//=2
    st=st[::-1]
    return st

def trans(n):
    n=n[::-1]
    su=0
    for i in range(len(n)):
        if n[i]=="1":
            su+=2**i
    return su

def solution(numbers):
    answer = []
    for num in numbers:
        p=binary(num)
        if num%2==0:
            answer.append(num+1)
        else:
            if p[0]=="1":
                p="0"+p
            p=list(p)
            for i in range(len(p)-1,-1,-1):
                if p[i]=="0":
                    p[i]="1"
                    p[i+1]="0"
                    break
            p="".join(p)
            su=trans(p)
            answer.append(su)
    return answer