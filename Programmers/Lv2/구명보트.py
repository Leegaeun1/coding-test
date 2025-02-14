def check(people,limit,cnt):
    st=0
    fin=len(people)-1
    while(1):
        if people[st]+people[fin]<=limit:
            st+=1
        cnt+=1
        fin-=1
        if st>fin:
            break        
    return cnt
def solution(people, limit):
    cnt = 0
    people.sort()
    cnt=check(people,limit,cnt)
    return cnt