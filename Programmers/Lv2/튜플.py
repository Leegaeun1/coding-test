def solution(s):
    s=s[2:-2]
    new_s=s.split("},{")
    li=[]
    result=[]
    for a in new_s:
        li.append(list(map(int,a.split(","))))
    li.sort(key=len)
    for a in li:
        for b in a:
            if b not in result:
                result.append(b)
    return result