def solution(pri, location):
    queue = [(priority, idx) for idx, priority in enumerate(pri)] # [우선순위, 순서인덱스] 형태로 저장함
    num=0 # 최종적으로 몇번째인지
    k=0 # 제거하거나 추가를 알수있는 값
    while(len(queue)>0): # 큐의 길이가 0보다 클때동안
        tmp=queue[0] # 기준 큐
        for i in queue[1:]: # 나머지큐
            if tmp[0]<i[0]: # 기준의 우선순위가 더 낮으면
                queue.append(queue.pop(0)) # 제거하고 추가
                k=1 # 바꼈다는걸 알려줌
                break
            else:
                k=0
        if(k==0): # 안바꼈을때는 첫번째 큐의 우선순위가 가장높다는것
            queue.pop(0) # 제거해줌
            num+=1
            if location==tmp[1]: # 찾는 location과 같으면
                return num # 몇번째인지