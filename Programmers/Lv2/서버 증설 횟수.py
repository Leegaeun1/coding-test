def solution(players, m, k):
    add_server=[0]*24
    cnt=0
    
    for i in range(24):
        p=players[i]//m
        
        if p>add_server[i]:
            tmp=p-add_server[i]
            cnt+=tmp
            if i+k<24:
                for j in range(i,i+k):
                    add_server[j]+=tmp
            else:
                for j in range(i,24):
                    add_server[j]+=tmp
    

    return cnt