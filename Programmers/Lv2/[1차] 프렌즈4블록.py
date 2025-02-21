def clear(m,n,board): # 삭제시키는 함수
    li,cnt=[],0
    for row in range(m-1):
        for col in range(n-1):
            if board[row][col]==board[row][col+1]==board[row+1][col]==board[row+1][col+1] and board[row][col]!="0": # 2x2가 같으면
                li.append((row,col))
                li.append((row,col+1))
                li.append((row+1,col))
                li.append((row+1,col+1))
    cnt=len(list(set(li))) # 총 없어질 개수
    for row,col in li:
        board[row][col]="0" # 없어지는거 0으로 바꾸기
    for col in range(n):
        empty = m - 1  # 블록이 떨어질 위치 (아래에서부터 채움)
        for row in range(m - 1, -1, -1):  # 아래에서 위로 탐색
            if board[row][col] != "0":  
                board[empty][col] = board[row][col]  # 블록을 아래로 이동
                if empty != row:
                    board[row][col] = "0"  # 기존 위치를 0으로 변경
                empty -= 1  # 다음 블록을 채울 위치를 한 칸 위로 이동

    return cnt,board
def solution(m, n, board):
    result=0
    board = [list(row) for row in board]
    cnt,board=clear(m,n,board)
    result+=cnt
    while(cnt!=0): # 터질게 없을때까지
        cnt,board=clear(m,n,board)
        result+=cnt
    return result