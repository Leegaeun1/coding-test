def solution(n, left, right):
    cnt=0
    li=[a for a in range(left,right+1)]
    for a in range(len(li)):
        li[a]= max(li[a]%n,li[a]//n)+1

    return li