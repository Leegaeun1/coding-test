from itertools import permutations

def operate(expression):
    operator=[]
    if '-' in expression:
        operator.append('-')
    if '+' in expression:
        operator.append('+')
    if '*' in expression:
        operator.append('*')
    return operator

def divide(expression): # 각 숫자와 연산자들로 나누기
    new_list=[]
    idx,front_idx=0,0
    while idx<len(expression):
        if expression[idx].isdigit() == False: # 연산자이면 
            new_list.append(expression[front_idx:idx]) # 앞의 숫자를 추가
            new_list.append(expression[idx]) # 연산자도 추가
            front_idx=idx+1
        idx+=1
    new_list.append(expression[front_idx:])
    return new_list

def calc(a,b,op): # 계산
    a,b= int(a),int(b)
    if op=="+":
        return a+b
    if op=="-":
        return a-b
    if op=="*":
        return a*b

def solution(expression):
    operator = operate(expression) # 표현식 안에 있는 연산자
    priorities = list(permutations(operator,len(operator))) # 연산자 우선순위
    new_exp=divide(expression) 
    exp_tmp=new_exp[:] # 처음 값 저장
    sums=[]
    
    for priority in priorities:
        new_exp= exp_tmp[:] # 처음 값 저장
        i=0 # 우선순위 
        while i<len(priority): # 우선순위대로 다 돌기
            stack=[] # 피연산자와 연산자 저장
            while True: 
                if new_exp[0].isdigit(): # 숫자이면 스택에 추가
                    stack.append(new_exp[0]) 
                else: # 연산자일때
                    if new_exp[0]==priority[i]: # 우선순위가 가장 높으면 
                        front=stack.pop() # 앞 숫자
                        stack.append(str(calc(front,new_exp[1],priority[i]))) # 앞 숫자와 뒤 숫자 연산한 값을 스택에 추가
                        del new_exp[:1]
                    else: # 우선순위가 낮으면 
                        stack.append(new_exp[0]) # 추가
                new_exp.pop(0) # 없애주기
                if len(new_exp)==0: # 비었으면 멈추기
                    break
            new_exp=stack # 스택의 값을 다시 저장해주기
            i+=1 # 1순위 제거
        sums.append(abs(int(new_exp[0]))) # 절대값을 저장
    return int(max(sums)) # 최댓값