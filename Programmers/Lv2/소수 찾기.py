import itertools
def isprime(n):
    n=int(n)
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def solution(numbers):
    cnt=0
    le=len(numbers)
    nPr =[]
    for i in range(1,le+1):
        nPr.extend(list(itertools.permutations(numbers, i)))
    for i in range(len(nPr)):
        nPr[i]="".join(nPr[i])
    nPr=list(set(map(int,nPr)))
    for i in nPr:
        if isprime(i)==True:
            cnt+=1
    return cnt