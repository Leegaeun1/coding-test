def solution(n):
    cnt=0 #개수
    p=1 #비교할 최소 값
    while True: 
        su=0 #반복할때마다 초기화
        for i in range(p,n+1):
            su+=i #값 더하기
            if su==n: #더한값들이 n과 같으면 cnt늘려주고 p도 늘려주고 break
                cnt+=1
                p+=1
                break
            if su>n: #더한 값들이 n보다크면 p늘리고 break. 
                p+=1
                break
        if p>n: #반복 다했는데 p가 n보다 크면 break
            break
    return cnt