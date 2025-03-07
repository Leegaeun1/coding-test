import heapq

def solution(N, road, K):
    an=[]
    graph=[[] for _ in range(N+1)]
    distance = [1e8] * (N+1)
    for a,b,c in road: # 그래프 생성
        graph[a].append((b, c))
        graph[b].append((a, c))
        
    def dijkstra(start):
        q = []
        heapq.heappush(q, (0, start)) # 최소 거리, 노드 번호
        distance[start] = 0

        while q:
            dist, now = heapq.heappop(q) 
            if distance[now] < dist: 
                continue               

            for i in graph[now]:    
                if dist+i[1] < distance[i[0]] and dist+i[1]<=K:
                    distance[i[0]] = dist+i[1]  
                    heapq.heappush(q, (dist+i[1], i[0]))
            
    dijkstra(1)
    for i in distance:
        if i!=1e8:
            an.append(i)
    #an=list(set(an))
    return len(an)