def solution(k, d):
    cnt = 0
    res = [i for i in range(0,d+1,k)]
    j = len(res) - 1 # 길이
    
    for i in range(len(res)):
        while j >= 0 and res[i]**2 + res[j]**2 > d**2: # 인덱스가 0이상, 길이가 d보다 크면 
            j -= 1 # 앞으로 이동
        if j < 0: # 인덱스 벗어나면 
            break
        cnt += j + 1
        
    return cnt