def solution(prices):
    le=len(prices)
    an= [0]*le
    for i in range(le):
        cnt=0
        for j in range(i+1,le):
            if prices[i]<=prices[j]:
                cnt+=1
            else:
                cnt+=1
                break
        an[i]=cnt
    return an