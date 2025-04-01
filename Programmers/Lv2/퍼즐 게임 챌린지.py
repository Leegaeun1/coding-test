def solution(diffs, times, limit):
    min_level = 1
    max_level = max(diffs)
    res = max_level

    while min_level < max_level: # 이진탐색
        mid_level = (min_level+max_level)//2
        time_prev = times[0] # 이전 퍼즐 걸리는 시간
        total_time = 0 # 전체 퍼즐 걸리는 시간 
        
        for i in range(len(diffs)):
            # diff <= level 일때 퍼즐 틀리지x time_cur 시간 사용하여 해결
            if diffs[i] <= mid_level:
                total_time += times[i]
            # diff > level 일때 diff - level 번 틀림. (time_cur + time_prev)*틀린 횟수 + time_cur 
            else:
                total_time += (time_prev + times[i]) * (diffs[i] - mid_level) + times[i]   
            time_prev = times[i] 
            
        if total_time > limit: # limit 보다 크면 숙련도가 더 높아야함 
            min_level = mid_level+1
        else:
            max_level = mid_level
            res = min(res,mid_level) # 더 낮은 숙련도
    return res