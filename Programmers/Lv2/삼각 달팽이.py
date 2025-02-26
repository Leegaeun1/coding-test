def clear(n): # 배열을 n행은 n열이 존재하도록 만들기
    answer = []
    cnt=0 # 몇번까지 존재하는가
    for i in range(1,n+1):
        li=[]
        for i in range(i):
            li.append(0)
            cnt+=1
        answer.append(li)
    return answer,cnt

def solution(n):
    answer,cnt=clear(n)
    num=2 # 2부터 시작
    row,col=0,0 # 행,열
    answer[0][0]=1 # 1은 미리 설정해두기
    new_list=[]
    while(num<=cnt): 
        while row<len(answer)-1 and answer[row+1][col]==0: # 아래로 이동
            row+=1
            answer[row][col]=num
            num+=1
        while col<len(answer[row])-1 and answer[row][col+1]==0: # 오른쪽으로 이동
            col+=1
            answer[row][col]=num
            num+=1
        while answer[row-1][col-1]==0: # 위로 이동(북서 방향으로 이동)
            row-=1
            col-=1
            answer[row][col]=num
            num+=1
    for i in answer: # 2차원배열을 1차원배열로 만들기
        for j in i:
            new_list.append(j)
    return new_list