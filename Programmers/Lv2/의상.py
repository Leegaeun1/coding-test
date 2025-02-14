def solution(clothes):
    le=len(clothes)
    dic={}
    answer=1
    for a in range(le):
        if clothes[a][1] not in dic:
            dic[clothes[a][1]]=1
        else:
            dic[clothes[a][1]]+=1
    value=list(dic.values())
    
    for a in value:
        answer*=(a+1)
    return answer-1
