def fibo(n):
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return b

def solution(n):
    answer = fibo(n)
    return answer%1000000007