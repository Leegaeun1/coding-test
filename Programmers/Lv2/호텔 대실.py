def solution(book_time):
    book_time.sort()
    room=[]
    for a,b in book_time:
        ischange=0  # 바꿔졌는지
        if len(room)==0: # 처음에는 퇴실 시간을 먼저 추가해줌
            room.append(b)
        else: # 방이 하나이상이면
            b_time=a.split(":") # 예약시간 나누기
            b_m=int(b_time[0])*60+int(b_time[1])
            for i in range(len(room)): # 사용하고 있는 방의 퇴실 시간
                time=room[i].split(":") # 퇴실시간 나누기
                m=int(time[0])*60+int(time[1]) 
                
                if b_m-m>=10: # 예약시간의 시가 퇴실시간의 시보다 클때
                    room[i]=b # 그 방의 퇴실시간을 업데이트해줌
                    ischange=1 # 바꿈
                    break

            if ischange==0: # 안바꼈을때 새로운방
                room.append(b)
            room.sort()
    return len(room)