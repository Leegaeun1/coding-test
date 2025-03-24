import heapq # 최대 힙 사용

def solution(n, k, enemy):
    max_heap = [] 
    stage=0
    for i in range(len(enemy)):
        heapq.heappush(max_heap, -enemy[i]) # 체력 큰 병사대로 저장하기
        n -= enemy[i] 
        
        if n<0: # 체력이 0보다 작을때
            if k>0: # 무적권이 있으면  
                k-=1 
                n += (-heapq.heappop(max_heap)) # 제일 체력이 많은 병사 체력을 더해줌
            else: # 없으면 종료
                return stage
        stage = i+1

    return stage