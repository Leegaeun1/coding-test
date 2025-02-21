from collections import deque

def bfs(x,y,n):
    queue=deque([(x,0)])
    cnt_list=[]
    visited = set()
    while queue:
        first=queue.popleft()
        if first[0]==y:
            cnt_list.append(first[1])
        elif first[0]<y:
            if first[0] not in visited:
                visited.add(first[0])
                queue.append((first[0]*2,first[1]+1))
                queue.append((first[0]*3,first[1]+1))
                queue.append((first[0]+n,first[1]+1))
    return cnt_list

def solution(x, y, n):
    answer = bfs(x,y,n)
    if len(answer)==0:
        return -1
    return min(answer)