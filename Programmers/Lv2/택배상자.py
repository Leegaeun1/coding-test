def solution(order):
    cnt = 0
    stack=[]
    num=1
    idx=0
    while(len(order)>idx):
        if order[0]>num:
            stack.append(num)
            num+=1
        elif order[0]==num:
            cnt+=1
            idx+=1
            num+=1
        else:
            if stack[-1]==order[idx]:
                cnt+=1
                stack.pop()
                idx+=1
            else:
                break
    return cnt 