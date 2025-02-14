def solution(num, target):
    global cnt
    cnt=0
    def dfs(sum,n):
        global cnt
        if n==len(num):
            if target==sum:
                cnt+=1
            return
        dfs(sum+num[n],n+1)
        dfs(sum-num[n],n+1)
    dfs(0,0)
    return cnt