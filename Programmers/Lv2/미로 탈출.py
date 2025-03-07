from collections import deque

def startPosition(maps,target): # 시작 위치 찾기
    pos=[]
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j] == target:
                pos = (i,j)
                break
        if len(pos)!=0:
            break
    return pos

def bfs(maps,pos,target):
    cnt=0
    m, n=len(maps), len(maps[0])
    visited = [[0]*n for _ in range(m)]
    queue = deque([(pos[0], pos[1], cnt)]) # 시작위치
    visited[pos[0]][pos[1]]=1 # 방문함
    direct=[(0,1),(1,0),(0,-1),(-1,0)]
    
    while queue:
        v = queue.popleft()
        x, y, cnt = v[0], v[1], v[2]
        if maps[x][y] == target:
            return cnt
            
        for dx, dy in direct:
            if 0 <= x + dx < len(maps) and 0 <= y + dy < len(maps[0]) and visited[x + dx][y + dy]==0 and maps[x+dx][y+dy] != "X":
                queue.append((x + dx, y + dy, cnt + 1))
                visited[x + dx][y + dy] = 1
    
    return -1

def solution(maps):
    start = startPosition(maps,"S")
    lever = startPosition(maps,"L")
    cnt_L=bfs(maps,start,"L")
    if cnt_L==-1:
        return -1
    cnt_E=bfs(maps,lever,"E")
    if cnt_E==-1:
        return -1
    
    
    return cnt_L+cnt_E