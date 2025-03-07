def solution(storey):
    cnt = 0
    while(storey>0):
        num=storey%10
        storey//=10
        if num>5:
            storey+=1
            cnt+=10-num
            
        elif num==5:
            if storey%10<5:
                cnt+=10-num
            else:
                storey+=1
                cnt+=num
        else:
            cnt+=num
    return cnt
