def solution(bridge_length, weight, truck_weights):
    time,idx = 0,0
    passing_truck=[] # 다리를 지난 트럭
    bridge_truck=[] # 다리를 건너는 트럭
    weight_sum=0
    while(idx<len(truck_weights) or bridge_truck):
        time+=1
        for i in range(len(bridge_truck)):
            bridge_truck[i][1]+=1
            
        if bridge_truck and bridge_truck[0][1]>bridge_length:
            weight_sum-=bridge_truck[0][0]
            passing_truck.append(bridge_truck.pop(0))
        
        if idx<len(truck_weights):
            if len(bridge_truck)<bridge_length and truck_weights[idx]+weight_sum<=weight:
                bridge_truck.append([truck_weights[idx],1])
                weight_sum+=truck_weights[idx]
                idx+=1
    return time
