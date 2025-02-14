def solution(ele):
    li=[]
    idx=2
    le=len(ele)
    for a in ele:
        if a not in li:
            li.append(a)
    while(idx<le):
        for a in range(0,le):
            cnt=0
            su=0
            if(le-a<idx):
                cnt=idx-(le-a)
            if(cnt!=0):
                su=sum(ele[:cnt])
                su+=sum(ele[a:])
            else:
                su+=sum(ele[a:a+idx])
            li.append(su)
        idx+=1
    li.append(sum(ele))
    li=set(li)
    return len(li)