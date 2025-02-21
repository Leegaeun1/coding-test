def solution(record):
    dic={}
    result=[]
    for enter in record:
        enters=enter.split(" ")
        if enters[0]!="Leave":
            dic[enters[1]]=enters[2]
    for enter in record:
        enters=enter.split(" ")
        if enters[0]=="Enter":
            result.append(f"{dic[enters[1]]}님이 들어왔습니다.")
        elif enters[0]=="Leave":
            result.append(f"{dic[enters[1]]}님이 나갔습니다.")
    return result