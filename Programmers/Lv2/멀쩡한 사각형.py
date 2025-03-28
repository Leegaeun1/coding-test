def gcd(a,b): #최대 공약수.유클리드 호제법 사용
    if a%b==0:
        return b
    return gcd(b,a%b)

def solution(w,h):
    res = w * h - (w + h - gcd(w, h))
    return res