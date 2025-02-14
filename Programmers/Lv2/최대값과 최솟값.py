def solution(s):
    answer = ''
    li=s.split()
    for i in range(len(li)):
        li[i]=int(li[i])
    answer+=str(min(li))+" "
    answer+=str(max(li))
    return answer