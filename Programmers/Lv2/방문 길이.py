def solution(dirs):
    dic={"U":[0,1],"D":[0,-1],"L":[-1,0],"R":[1,0]}
    x,y=0,0
    stack=[[0,0]]
    cnt=0
    for i in dirs:
        if -5<x<5 or (x==5 and dic[i][0]==-1) or (x==-5 and dic[i][0]==1):
            x+=dic[i][0]
        if -5<y<5 or (y==5 and dic[i][1]==-1) or (y==-5 and dic[i][1]==1):
            y+=dic[i][1]
        for j in range(len(stack)-1):
            if [x,y]==stack[j]:
                #print(x,y,j,stack[j-1],stack[-1])
                if j>0:
                    if stack[j-1]==stack[-1] or stack[-1]==stack[j+1]:
                        cnt+=1
                        break
                else:
                    if stack[-1]==stack[j+1]:
                        cnt+=1
                        break
        if [x,y]!=stack[-1]:
            stack.append([x,y])                  
    return len(stack)-1-cnt