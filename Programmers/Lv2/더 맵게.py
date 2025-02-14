import heapq
def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville)
    while(scoville[0]<K and len(scoville)>1):
        f=heapq.heappop(scoville)
        q=heapq.heappop(scoville)
        heapq.heappush(scoville,f+q*2)
        cnt+=1
    if min(scoville)<K:
        return -1
    return cnt