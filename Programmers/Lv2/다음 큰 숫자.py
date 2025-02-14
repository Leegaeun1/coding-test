def solution(n):
    s="" #이진수 저장
    p=n #p에 n값저장
    while(p>0): #p로 이진수 만들기
        s+=str(p%2)
        p//=2
    one=s.count("1") #n의 이진수에서 1개수 세기
    while(1):
        t="" #이진수 저장할 공간
        n+=1 #n의값늘리면서 보기
        m=n #m으로 이진수 만들기
        while(m>0):
            t+=str(m%2)
            m//=2
        one2=t.count("1") #m의 1의값세기
        if one2==one: #1의값 같으면 바로 리턴
            return n
