from collections import deque

def bfs(start,maps):
    n,m=len(maps),len(maps[0]) # n행 m열
    visited=[[0]*m for _ in range(n)] # 방문여부
    queue=deque([(start[0],start[1],1)]) # 큐생성
    visited[start[0]][start[1]]=1 # 방문함
    direct=[(1,0),(0,1),(-1,0),(0,-1)] # 아래,오른쪽,위,왼쪽 순서대로
    while queue:
        v=queue.popleft() # 큐 반환
        x,y,cnt=v[0],v[1],v[2] 
        if x==n-1 and y==m-1: # 상대 진영에 도달하면
            return cnt
        for a in direct: 
            if 0<=x+a[0]<n and 0<=y+a[1]<m and visited[x+a[0]][y+a[1]]==0 and maps[x+a[0]][y+a[1]]==1: # 방향을 움직였을때 0이상 n또는 m미만, 방문하지않고 벽이 아닐때
                queue.append([x+a[0],y+a[1],cnt+1]) # 큐에 추가
                visited[x+a[0]][y+a[1]]=1 # 방문여부
    return -1
def solution(maps):
    cnt=bfs((0,0),maps)
    return cnt