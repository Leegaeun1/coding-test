cnt_list = []

def dfs(graph, v, visited): 
    global cnt
    visited[v] = True  # 방문 처리
    for i in graph[v]:  # v번 노드와 연결된 노드들
        if not visited[i]:  # 방문하지 않았으면
            cnt += 1
            dfs(graph, i, visited)  # 재귀 호출하여 계속 탐색

def solution(n, wires):
    global cnt, cnt_list
    cnt_list = []
    graph = [[] for i in range(n + 1)]
    
    # 양방향 그래프 생성
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
    
    # 각 간선을 하나씩 끊어보며 연결 요소 크기 차이 계산
    answer = n
    for a, b in wires:
        # 간선 제거
        graph[a].remove(b)
        graph[b].remove(a)
        
        # 방문 여부 초기화
        visited = [False] * (n + 1)
        cnt = 1  # 시작 노드 포함
        dfs(graph, 1, visited)  # 1번 노드에서 DFS 시작
        part1 = cnt  # 첫 번째 연결 요소 크기
        part2 = n - cnt  # 두 번째 연결 요소 크기
        
        # 두 연결 요소 간의 차이의 최소값 갱신
        answer = min(answer, abs(part1 - part2))
        
        # 제거한 간선 복구
        graph[a].append(b)
        graph[b].append(a)
    
    return answer
