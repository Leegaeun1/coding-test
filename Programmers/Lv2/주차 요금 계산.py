def car(records):
    dic={} # IN일때 시간을 저장할 공간
    cars=[] # records의 정보를 새로 저장하기
    an={} # 누적 시간 저장
    for i in records: # 차량번호를 딕셔너리에 저장
        li=i.split(" ")
        time=li[0].split(":")
        li[0]=int(time[0])*60+int(time[1]) # 0시부터 분단위로 표현한 것
        cars.append(li)
        dic[li[1]]=-1 
        an[li[1]]=0
    return dic,cars,an

def solution(fees, records):
    dic,cars,an=car(records)
    result=[]
    for i in cars:
        if i[-1]=="IN":
            dic[i[1]]=i[0]  
        else:
            an[i[1]]+=i[0]-dic[i[1]]
            dic[i[1]]=-1
    for i in cars:
        if dic[i[1]]!=-1: # IN은 저장되었으나 OUT이 없을경우
            an[i[1]]+=23*60+59-dic[i[1]]
            dic[i[1]]=-1
    an=sorted(an.items()) # 차량 번호순으로 정렬
    
    for c in an:
        time=c[1]-fees[0]
        if time<=0:
            time=0
        else:
            if time%fees[2]!=0:
                time+=fees[2]
        result.append(fees[1]+int((time/fees[2]))*fees[3])
    return result