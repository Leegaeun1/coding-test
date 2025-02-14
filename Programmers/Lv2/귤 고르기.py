def solution(k, tan):
    dic={}
    tan_set=set(tan) #집합으로 저장하기
    li=[] # 딕셔너리의 값을 저장할곳
    cnt=0 #개수 저장
    for a in tan_set: #딕셔너리에 값 추가
        dic[a]=0
    for a in tan: #개수 추가
        dic[a]+=1
    for key,value in dic.items():
        li.append(value) # 개수를 리스트로 저장 
    li.sort(reverse=True) # 내림차순
    while(k>0):
        k-=li[cnt] 
        cnt+=1
    return cnt