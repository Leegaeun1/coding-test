def position(places): # P인 좌표 저장하기
    pos = []
    for i in range(5):
        tmp = []
        for j in range(5):
            places_tmp = list(places[i][j])
            for k in range(5):
                if places_tmp[k] == 'P':
                    tmp.append([j,k])
        pos.append(tmp)
    return pos

def solution(places):
    res = []
    pos = position(places) # P인 좌표
    rnum = 0
    # 좌표들 하나씩 비교하기
    for row_num in pos: # 각 행
        isOverlap = 0 # 겹친게 있는지
        for i in range(len(row_num)): 
            r1, c1 = row_num[i]
            for j in range(i+1,len(row_num)):
                r2, c2 = row_num[j]
                
                if abs(r1 - r2) + abs(c1 - c2) <= 2: # 맨해튼거리가 2이하일때
                    # 같은행에서 거리가 2일때
                    if r1==r2: # 같은 행일때
                        if places[rnum][r1][(c1+c2)//2] != 'X': # 파티션이 아니라면
                            isOverlap = 1 
                    
                    # 같은열에서 거리가 2일떄
                    elif c1==c2: # 같은 열일때
                        if places[rnum][(r1+r2)//2][c1] != 'X': # 파티션이 아니라면
                            isOverlap = 1 
                    
                    # 대각선으로 거리가 2일때
                    elif places[rnum][r1][c2] != 'X' or places[rnum][r2][c1] != 'X':
                        isOverlap = 1 

        if isOverlap == 1:
            res.append(0)
        else:
            res.append(1)
    
        rnum += 1
    return res