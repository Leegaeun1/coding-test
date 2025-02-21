def solution(number, k):
    stack = []
    for num in number:
        # 스택이 비어있지 않고, 현재 숫자가 스택의 마지막 숫자보다 크며, 제거할 수 있는 횟수가 남아있을 때
        while stack and k > 0 and stack[-1] < num:
            stack.pop()  # 스택의 마지막 숫자 제거
            k -= 1
        stack.append(num)  # 현재 숫자 추가
    if k > 0:# 아직 제거할 숫자가 남아있다면 뒤에서 제거
        stack = stack[:-k]

    return ''.join(stack)
