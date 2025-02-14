def solution(A,B):
    an=0
    A.sort() #오름차순정렬
    B.sort(reverse=True) #내림차순 정렬
    for i in range(len(A)):
        an+=(A[i]*B[i]) 
    return an