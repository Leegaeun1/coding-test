from collections import deque

def solution(board):
    m, n=len(board), len(board[0]) # 행, 열
    visited=[[False]*n for _ in range(m)]
    start = [0, 0] # 시작 위치(R)
    arrive = [0, 0] # 도착 위치(G)

    
    for i in range(len(board)): # R의 위치 찾기
        if 'R' in board[i]:
            start = [i, board[i].index('R')] # 행, 열 저장
            break

    def move(direct, x, y, cnt): # 닿을때 까지 이동시키기 
        origin_x, origin_y= x, y
        dx, dy= direct[0], direct[1]
        while True:
            if 0 <= x + dx < m and 0 <= y + dy < n and visited[x + dx][y + dy]: # 만약 이미 도착했던곳이라면 가지 못하도록
                return 0
            if 0 <= x + dx < m and 0 <= y + dy < n and board[x + dx][y + dy] != "D": 
                x += dx
                y += dy
            else:
                break
        if [origin_x,origin_y] == [x,y]: # 이동하지 않았으면 
            return 0
        return [x, y, cnt+1] # 도달한 x,y와 횟수 저장
    
    def bfs(board, start):
        queue = deque([(start[0],start[1],0)]) # 큐 생성
        visited[start[0]][start[1]] = True # 방문 처리
        direction = [(1,0),(-1,0),(0,-1),(0,1)] # 이동 방향
        cnt=0 # 진행 횟수
        
        while queue:
            pop_x, pop_y,cnt = queue.popleft() 
            visited[pop_x][pop_y] = True
            if board[pop_x][pop_y]== "G": # 도착지점
                return cnt
                
            for i in direction:
                arrive = move(i, pop_x, pop_y,cnt)
                if arrive !=0 : 
                    queue.append(arrive)
        return -1
    
    cnt = bfs(board, start)
    return cnt