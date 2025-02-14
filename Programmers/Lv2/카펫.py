def solution(brown, yellow):
    li = [0,0]
    div=[]
    for a in range(1,yellow+1):
        if yellow%a==0:
            if(2*(yellow//a+a)==brown-4):
                li[0]=a+2
                li[1]=yellow//a+2
    li.sort(reverse=True)
    return li