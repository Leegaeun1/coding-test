def lcm(a,b):
    return a*b//gcd(a,b)

def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

def solution(arr):
    answer=arr[0]
    for num in arr[1:]:
        answer=lcm(answer,num)
    return answer