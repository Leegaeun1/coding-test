from collections import Counter
def solution(want, number, discount):
    dic={}
    ans=0
    for a in range(len(want)):
        dic[want[a]]=number[a]
    for a in range(0,len(discount)-9):
        count=Counter(discount[a:a+10])
        if dic==count:
            ans+=1

    return ans