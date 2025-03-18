def solution(data, col, row_begin, row_end):
    idx=0
    S_i=[]
    # col번째 컬럼 값을 기준으로 오름차순. 동일한 경우 내림차순
    sort_data1= sorted(data, key= lambda x: (x[col-1],-x[0]))
    
    # 정렬한 데이터에서 S_i= i번째 행의 튜플의 각 컬럼의값 %i 들의 합. 
    for i in range(row_begin-1,row_end):
        tmp = 0
        for j in sort_data1[i]:
            tmp += j%(i+1)
        S_i.append(tmp)
    res=S_i[0]
    
    # row_begin<=i<=row_end인 s_i들 XOR하기 
    for i in range(1,len(S_i)):
        res=res^S_i[i]
    return res