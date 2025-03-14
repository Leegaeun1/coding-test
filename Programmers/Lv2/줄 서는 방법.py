def solution(n, k):
    res=[]
    li = [i for i in range(1,n+1)] # [1,2,...,n]
    
    while len(li)>0:
        total=1
        for i in range(1,len(li)+1): # 팩토리얼
            total*=i
        total//=len(li) # 첫번째 숫자가 몇번씩 있는지? (n이 3이면 1로 시작하는게 두번, 2로 시작하는것도 두번..)
        target_first = k//total # 결과의 처음 숫자 
        if k%total==0: # 0으로 나누어떨어질때
            target_first-=1
        tmp=li[target_first] 
        li.remove(tmp) 
        res.append(tmp)
        k=k % total
        
    return res