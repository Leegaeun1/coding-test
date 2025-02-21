from collections import deque

def solution(queue1, queue2):
    queue1=deque(queue1)
    queue2=deque(queue2)
    sum1=sum(queue1)
    sum2=sum(queue2)
    sum_all=sum1+sum2
    cnt = 0
    if max(queue1+queue2)>(sum_all)//2 or sum_all%2!=0: # 합이 홀수거나 max값이 합//2보다 크면 불가능
        return -1
    target=sum_all//2
    max_oper=len(queue1)*5
    while(cnt<=max_oper):
        if sum1==target:
            return cnt
        if sum1>target: # 1이 더 크면 
            pop=queue1.popleft()
            sum1-=pop
            sum2+=pop
            queue2.append(pop)
        else: # 2이 더 크면
            pop=queue2.popleft()
            sum1+=pop
            sum2-=pop
            queue1.append(pop)
        cnt+=1
    return -1