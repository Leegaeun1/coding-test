
def gcd(a,b): #최대 공약수.유클리드 호제법 사용
    if a%b==0:
        return b
    return gcd(b,a%b)

def gcd_list(a):
    res=a[0]
    for i in a[1:]:
        res=gcd(res,i)
    return res

def get_divisors(n): # 약수들 저장 
    divisors = set()
    for i in range(1, int(n**0.5) + 1): 
        if n % i == 0:
            divisors.add(i) # 나눠지는수랑 
            divisors.add(n // i) # 짝인 수도 추가해주기
    divisors=sorted(divisors, reverse=True) # 내림차순으로 저장
    return divisors

def comp(divisors, array):
    for d in divisors:
        if all(num % d != 0 for num in array): # 나누어 떨어지지 않는것
            return d
    return 0

def solution(arrayA, arrayB):
    answer = 0
    li_A,li_B=gcd_list(arrayA),gcd_list(arrayB)
    divisorsA=get_divisors(li_A)
    divisorsB=get_divisors(li_B)
    return max(comp(divisorsA, arrayB), comp(divisorsB, arrayA))