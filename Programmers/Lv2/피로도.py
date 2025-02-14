visited=[]
def dfs(k,dungeons,cnt):
    max_cnt=cnt
    for i in range(len(dungeons)):
        if i not in visited and dungeons[i][0]<=k:
            visited.append(i)
            max_cnt=max(max_cnt,dfs(k-dungeons[i][1],dungeons,cnt+1))
            visited.pop()
    return max_cnt

def solution(k, dungeons):
    cnt=dfs(k,dungeons,0)
    return cnt