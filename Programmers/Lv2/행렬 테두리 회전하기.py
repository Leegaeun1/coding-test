def init(rows,columns): # 처음 행렬 초기화  
    matrix = []
    for i in range(rows):
        tmp=[]
        for j in range(1,columns+1):
            tmp.append(i*columns  + j)
        matrix.append(tmp)
    return matrix

def solution(rows, columns, queries):
    res = []
    matrix = init(rows, columns)
    for i in queries:
        x1,y1,x2,y2=i[0]-1,i[1]-1,i[2]-1,i[3]-1
        
        prev_value = matrix[x1][y1] # 회전 전 왼쪽 위 값 저장
        min_num = prev_value # 최솟값
        
        for i in range(y1+1, y2+1): # 오른쪽으로
            matrix[x1][i], prev_value = prev_value, matrix[x1][i]
            min_num = min(min_num, prev_value)
        
        for i in range(x1+1, x2+1): # 아래로
            matrix[i][y2], prev_value = prev_value, matrix[i][y2]
            min_num = min(min_num, prev_value)
        
        for i in range(y2-1, y1-1, -1): # 왼쪽으로
            matrix[x2][i], prev_value = prev_value, matrix[x2][i]
            min_num = min(min_num, prev_value)
        
        for i in range(x2-1, x1-1, -1): # 위쪽으로 
            matrix[i][y1], prev_value = prev_value, matrix[i][y1]
            min_num = min(min_num, prev_value)
        
        res.append(min_num) # 최솟값 저장하기
    return res