def el(a,n):
    return [a%n+1,(a//n)+1]

def solution(n, words):
    li=[words[0]]
    for a in range(1,len(words)):
        if words[a] not in li:
            if li[-1][-1]==words[a][0]:
                li.append(words[a])
            else:
                return el(a,n);
        else:
            return el(a,n);
    return [0,0]