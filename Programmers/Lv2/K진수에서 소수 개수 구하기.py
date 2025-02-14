import math
def isprime(num): # 소수인지 판별
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def translate(n,k): # k진수로 변환
    st = ''
    while n > 0:
        st += str(n % k)
        n //= k
    return st[::-1]

def check(n):
    zero=n.split('0') # 0기준으로 나누어 소수인지 비교하기
    cnt=0
    for i in zero:
        if i!='':
            if isprime(int(i)):
                cnt+=1
    return cnt
    
def solution(n, k):
    n=translate(n,k)
    return check(n)