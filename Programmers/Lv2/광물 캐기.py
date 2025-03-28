def solution(picks, minerals):
    res = 0
    d_p = {'diamond' : 1, 'iron' : 1, 'stone' : 1}
    i_p = {'diamond' : 5, 'iron' : 1, 'stone' : 1}
    s_p = {'diamond' : 25, 'iron' : 5, 'stone' : 1}
    
    total_picks = sum(picks)
    # 광물 그룹화
    minerals_group = []
    for idx in range(0,len(minerals),5):
        minerals_group.append(minerals[idx:idx+5])
        if len(minerals_group) == total_picks: # 곡괭이의 수만큼 있다면 멈추기
            break
    
    # 피로도 높은 순서대로 그룹 정렬하기 
    def group_sort(group):
        su = 0
        for m in group:
            su += s_p[m] # stone으로 캤을때 피로도
        return su
    
    minerals_group.sort(key = group_sort, reverse= True)
    
    # 광물 캐기
    for i in minerals_group:
        if picks[0] > 0:
            picks[0] -= 1
            for m in i:
                res += d_p[m]
        elif picks[1] > 0:
            picks[1] -= 1
            for m in i:
                res += i_p[m]
        elif picks[2] > 0:
            picks[2] -= 1
            for m in i:
                res += s_p[m]

    return res