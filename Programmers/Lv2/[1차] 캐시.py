def solution(cacheSize, cities):
    answer = 0
    cache=[]
    for a in cities:
        if a in cache:
            cache.remove(a)
            cache.append(a)
            answer+=1
        else:
            if(len(cache)==cacheSize and cacheSize>0):
                cache.pop(0)
            if (cacheSize>0):
                cache.append(a)
            answer+=5
        
    return answer