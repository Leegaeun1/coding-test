from collections import Counter
def solution(topping):
    cnt=0
    me=Counter(topping)
    bro={}
    for top in topping:
        me[top]-=1
        if top not in bro:
            bro[top]=1
        else:
            bro[top]+=1
        if me[top]==0:
            del me[top]
        if len(me)==len(bro):
            cnt+=1
        elif len(me)<len(bro):
            break
    return cnt