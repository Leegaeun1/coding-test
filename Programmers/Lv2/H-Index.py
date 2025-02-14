def solution(cit):
    answer=0
    cit.sort()
    le=len(cit)
    h=0
    while(h<cit[-1]):
        for i in range(le):
            if(cit[i]>=h and le-i>=h):
                answer=h
        h+=1
    return answer