from collections import Counter

def solution(weights):
    cnt = 0
    weight_count = Counter(weights)  # 무게별 개수 저장

    # 동일한 무게 쌍 처리
    for w, c in weight_count.items():
        if c > 1:
            cnt += c * (c - 1) // 2

    # 가능한 비율 쌍 탐색
    ratios = [(2, 3), (1, 2), (3, 4)]
    for w in weights:
        for a, b in ratios:
            if (w * b) % a == 0:  # 나누어떨어질 때만 탐색
                target = (w * b) // a
                if target in weight_count:
                    cnt += weight_count[target]

    return cnt
