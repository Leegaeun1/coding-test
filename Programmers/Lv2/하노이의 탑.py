def solution(n):
    res = []
    
    def hanoi(disks, start, end, tmp):
        if disks == 1:
            res.append([start, end])
        else:
            hanoi(disks-1, start, tmp, end) # 원반->보조
            hanoi(1, start, end, tmp) # 가장 큰 원반 이동
            hanoi(disks-1, tmp, end, start) # 보조->목표
             
    hanoi(n, 1, 3, 2)
    return res