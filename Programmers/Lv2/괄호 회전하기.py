def correct(s):
    li=[]
    cnt=0
    for a in s:
        if(a=='(' or a=='[' or a=='{'):
            li.append(a)
            cnt=2
        else:
            if(len(li)!=0):
                if a==')' and li[-1]=='(':
                    li.pop()
                elif a==']' and li[-1]=='[':
                    li.pop()
                elif a=='}' and li[-1]=='{':
                    li.pop()
                else:
                    break
    if len(li)==0 and cnt!=0:
        cnt=1
    else:
        cnt=0
    return cnt

def solution(s):
    an=0
    s=list(s)
    le=len(s)
    for a in range(le):
        an+= correct(s)
        pop=s.pop(0)
        s.append(pop)
    return an