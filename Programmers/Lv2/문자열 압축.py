def solution(s):
    l = len(s) # 문자열 길이
    res = []
    prev = ''
    # 1~l개 단위로 잘라서 압축한 결과들을 저장하기
    for i in range(1,l+1): # 총 길이만큼 반복
        cnt = 1
        new_str = ''
        for j in range(0,l,i): # i개 단위로 잘라주기 
            cur = s[j:j+i]
            if j == 0:
                prev = cur
                continue
            if prev == cur: # 자른게 앞에 자른것과 같으면 갯수 더해주고
                cnt += 1
            else: # 다를때 갯수+문자열을 새로운 문자열에 더해주기.
                if cnt>1:
                    new_str += str(cnt) + prev
                else:
                    new_str += prev
                cnt = 1
            prev = cur
        if cnt>1:
            new_str += str(cnt) + prev
        else:
            new_str += prev
        res.append(len(new_str)) #문자열이 끝나면 그 결과를 저장하기
    return min(res)