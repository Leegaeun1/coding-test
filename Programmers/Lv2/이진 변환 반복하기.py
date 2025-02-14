def solution(s):
    re = [0,0] #[몇번변환, 몇개 삭제]
    while(s!="1"): #1이 아닐동안
        s_z=len(s)-s.count("0") #제거한 수 구하기
        re[1]+=s.count("0") #삭제한 개수 더해주기
        s="" #문자열 초기화
        while(s_z>0): #이진법 
            s+=str(s_z%2)
            s_z//=2
        re[0]+=1 #변환할때마다 1증가
    return re