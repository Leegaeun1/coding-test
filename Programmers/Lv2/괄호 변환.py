def iscorrect(st): # 올바른 문자열인지
    stack = []
    for i in st: 
        if i == '(':
            stack.append(i)
        else:
            if len(stack)>0:
                stack.pop()
            else:
                return False
    if len(stack)==0:
        return True


def isbalance(st): # 균형잡힌 괄호 문자열 찾기
    left, right =0, 0
    for i in range(len(st)):
        if st[i] == '(':
            left += 1
        else:
            right += 1
        if left == right: # 개수가 같아졌을때
            return st[:i+1], st[i+1:]

def repeat(p):
    if len(p)==0: # 빈 문자열이면 
        return ""
    u, v = isbalance(p)
    if iscorrect(u): # 올바른 문자열인가?
        return u+ repeat(v)
    else:
        res = "(" + repeat(v) + ")"
        remove = u[1:-1]
        remove=remove.replace('(','_') # (과 ) 변환
        remove=remove.replace(')','(')
        remove=remove.replace('_',')')
        return res + remove
    
def solution(p):
    if iscorrect(p): # 올바른 문자열인가?
        return p

    return repeat(p)