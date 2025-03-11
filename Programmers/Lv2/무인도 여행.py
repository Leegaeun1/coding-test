from collections import deque

def solution(maps):
    li=[]
    m,n=len(maps),len(maps[0]) # m행 n열
    visited= [[False]*n for _ in range(m)]
    direct=[[1,0],[0,1],[-1,0],[0,-1]] # 아래 오른쪽 위 왼쪽    
    
    for i in range(m):
        maps[i]=list(maps[i])
    
    def dfs(x,y):
        queue=deque([(x,y)])
        visited[x][y]=True # 방문처리
        cnt=int(maps[x][y])
        while queue:
            x,y=queue.popleft()
            for dx,dy in direct:
                if 0<=x+dx<m and 0<=y+dy<n and maps[x+dx][y+dy]!="X" and not visited[x+dx][y+dy]:
                    visited[x+dx][y+dy]=True # 방문처리
                    queue.append([x+dx,y+dy])
                    cnt+=int(maps[x+dx][y+dy])    

        li.append(cnt)
            
    for i in range(m):
        for j in range(n):
            if not visited[i][j] and maps[i][j]!="X":
                dfs(i,j)
    li.sort()            
    if len(li)==0:
        return [-1]
    
    return li