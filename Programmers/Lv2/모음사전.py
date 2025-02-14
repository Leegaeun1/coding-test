def solution(word):
    global cnt
    cnt=0
    def dfs(st):
        global cnt
        if len(st)==6:
            return
        if st==word:
            return cnt
        cnt+=1
        for char in ['A', 'E', 'I', 'O', 'U']:
            result = dfs(st + char)
            if result is not None:
                return result  # 원하는 값을 찾으면 즉시 반환
        return None  # 끝까지 못 찾으면 None 반환
    cnt=dfs('')
    return cnt