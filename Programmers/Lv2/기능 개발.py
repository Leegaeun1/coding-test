def solution(pro, speeds):
    le=len(pro)
    li = []
    cnt=[0]*le
    answer=1
    idx=0
    while(min(pro)<100):
        for i in range(le):
            pro[i]+=speeds[i]
            if(pro[i]<100):
                cnt[i]+=1
    while(sum(li)<le):
        for i in range(idx+1,len(cnt)):
            if(cnt[idx]>=cnt[i]):
                answer+=1
            else:
                break
        li.append(answer)
        idx+=answer
        answer=1
    return li