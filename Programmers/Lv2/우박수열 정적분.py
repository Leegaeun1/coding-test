def makeOne(k): # 반복하여 1로 만들기
    num = [k]
    while k!=1:
        if k % 2 == 0:
            k = k // 2
        else:
            k = k * 3 + 1
        num.append(k)
    return num

def solution(k, ranges):
    num = makeOne(k) 
    n = len(num) - 1 # k가 초항인 우박수열이 1이 될때 까지의 횟수
    res = []
    for x,y in ranges: # 범위 내의 넓이 구하기
        sums = 0
        for i in range(x,n+y):
            mi = min(num[i],num[i+1]) # 두 점 중 작은 수
            ma = max(num[i],num[i+1]) # 두 점 중 큰 수
            sums += mi + ((ma-mi)/2) # 사각형 + 삼각형
        if x>n+y: # 끝점이 첫점보다 작을때 -1
            res.append(-1.0)
        else:
            res.append(float(sums))
    
    return res