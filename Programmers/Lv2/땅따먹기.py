def solution(land):
    sum_list=[[0]*4 for _ in range(len(land))]
    sum_list[0]=land[0]
    for i in range(1,len(land)):
        for j in range(4):
            li=[0]*4
            ma=0
            for k in range(4):
                if j!=k :
                    #print(sum_list[i-1][k],land[i][j])
                    p=sum_list[i-1][k]+land[i][j]
                    if p>ma:
                        li[j]=p
                        ma=p
            sum_list[i][j]=max(li)
    return max(sum_list[-1])