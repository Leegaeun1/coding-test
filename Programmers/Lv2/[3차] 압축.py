def solution(msg):
    li=[]
    for i in range(65,91): # A~Z까지 저장하기
        li.append(chr(i)) # 아스키코드
    an = [] # 출력할 값들
    i=0
    while(i<len(msg)):
        j=2
        k=1
        le=len(li)
        while(i+j<=len(msg)):
            if msg[i:i+j] not in li:
                li.append(msg[i:i+j])
                break
            j+=1
            k+=1
        if le==len(li):
            an.append(li.index(msg[i:i+j])+1)
        else:
            an.append(li.index(msg[i:i+j-1])+1)
        i+=k
    return an