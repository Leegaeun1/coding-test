def quad(arr,x,y,size,dic):
    isCombine=True
    begin=arr[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if arr[i][j]!=begin:
                isCombine=False
        if isCombine==False:
            break
    if isCombine:
        dic[str(begin)]+=1
        return;
    
    new_size=int(size*0.5)
    quad(arr,x,y,new_size,dic)
    quad(arr,x,y+new_size,new_size,dic)
    quad(arr,x+new_size,y,new_size,dic)
    quad(arr,x+new_size,y+new_size,new_size,dic)

def solution(arr):
    dic={"0":0,"1":0}
    size=len(arr[0])
    quad(arr,0,0,size,dic)
    return [dic["0"],dic["1"]]