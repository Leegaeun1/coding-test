def solution(n, t, m, p):
    dic={"10":"A","11":"B","12":"C","13":"D","14":"E","15":"F"}
    st='0'
    num=1
    while(len(st)<t*m):
        k=num
        new_st=''
        while(k>0):
            string=str(k%n)
            if string in dic:
                new_st+=dic[string]
            else:
                new_st+=string
            k//=n
        st+=new_st[::-1]
        num+=1
    return st[p-1:t*m:m]