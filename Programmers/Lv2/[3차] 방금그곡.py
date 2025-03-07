def change(st):
    new_st=''
    if "#" not in st:
        return st
    melody={"A":"U","B":"V","C":"W","D":"X","F":"Y","G":"Z","E":"I"}
    li=st.split("#")
    for i in range(len(li)-1):
        for j in range(len(li[i])-1):
            new_st+=li[i][j]
        new_st+=melody[li[i][-1]]
    new_st+=li[-1][:]
    return new_st

def solution(m, musicinfos):
    li=[]
    m=change(m)
    mLen=len(m)
    
    for info in musicinfos:
        st = info.split(",")
        start,fin,name,music = st[0],st[1],st[2],st[3]
        music=change(music)
        startTime,finTime = start.split(":"),fin.split(":")
        timediff = int(finTime[0])*60 + int(finTime[1]) - int(startTime[0])*60 - int(startTime[1]) # 몇분 동안 재생했는지
        musicLen = len(music) # 멜로디 길이 
        music = music*(timediff//musicLen) + music[:timediff%musicLen]
        if m in music:
            li.append([timediff,name])
    
    if len(li)!=0:
        li = sorted(li, key = lambda x: x[0], reverse=True) # 시간을 내림차순으로
        return li[0][1]
    
    return "(None)"