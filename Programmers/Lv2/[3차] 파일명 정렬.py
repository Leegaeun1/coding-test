def f(files): # head,number,tail 나누기
    head,number,tail=[],[],[]
    for name in files:
        idx,cnt=-1,0
        for i in range(len(name)):
            if name[i].isdigit():
                if idx==-1:
                    idx=i
                cnt+=1
            if name[i]==".":
                break
        head.append(name[:idx])
        number.append(name[idx:idx+cnt])
        tail.append(name[idx+cnt:])
    return head,number,tail

def solution(files):
    le=len(files)
    head,number,tail=f(files)
    
    for i in range(le-1):
        for j in range(le-1):
            if head[j].lower()>head[j+1].lower():
                head[j],head[j+1]=head[j+1],head[j]
                number[j],number[j+1]=number[j+1],number[j]
                tail[j],tail[j+1]=tail[j+1],tail[j]
            elif head[j].lower()==head[j+1].lower():
                if int(number[j])> int(number[j+1]):
                    head[j],head[j+1]=head[j+1],head[j]
                    number[j],number[j+1]=number[j+1],number[j]
                    tail[j],tail[j+1]=tail[j+1],tail[j]
    for i in range(le):
        files[i]=head[i]+number[i]+tail[i]
    return files