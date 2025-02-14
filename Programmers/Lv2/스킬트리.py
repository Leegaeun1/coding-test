def solution(skill, skill_trees):
    an=0
    for i in skill_trees:
        idx=0
        cnt=0
        for alpha in i:
            if idx<len(skill):
                if alpha==skill[idx]:
                    idx+=1
            if alpha in skill:
                cnt+=1
        if cnt==idx:
            an+=1
    return an