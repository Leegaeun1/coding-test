def solution(sequence, k):
    li=[]
    start,end=0,0
    mi= float('inf')
    su=sequence[0]
    while(start<len(sequence) and end<len(sequence)):
        if su==k: # 같을때 인덱스 저장
            if mi>end-start:
                mi=end-start
                li=[start,end]
            su-=sequence[start]
            start+=1
        elif su<k: # 적을때 end 뒤로 옮김
            end+=1
            if end<len(sequence):
                su+=sequence[end]
            
        else: # 클때는 start를 뒤로 옮김
            su-=sequence[start]
            start+=1
    return li