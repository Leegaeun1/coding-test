from itertools import combinations

def change(comb):
    li=[]
    for i in comb:
        li.append(''.join(i))
    return li

def solution(orders, course):
    res=[]
    an=[]
    for num in course:   
        orderDic={}
        ma=2
        lis=[]
        for food in orders:
            food=list(food)
            food.sort()
            comb= list(combinations(food,num))
            li=change(comb)
            for d in li: # 개수 세기
                if d not in orderDic:
                    orderDic[d]=1
                else:
                    orderDic[d]+=1
        for d in orderDic:
            if ma<orderDic[d]: # 최대값보다 크면 
                ma=orderDic[d] # 갱신
                lis=[] # 초기화
                lis.append(d) # 추가
            elif ma==orderDic[d]: # 최대랑 같으면 추가
                lis.append(d)
        if len(lis)>0:
            res.append(lis)
    for i in res:
        for j in i:
            an.append(j)
    an.sort()
    return an