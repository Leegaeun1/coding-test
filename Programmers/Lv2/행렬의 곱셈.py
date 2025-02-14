def mul(X,Y):
    return sum(x*y for x,y in zip(X,Y))

def solution(X, Y):
    answer = []
    for x_row in X:
        answer_row=[]
        for y_col in zip(*Y):
            answer_row.append(mul(x_row,y_col))
        answer.append(answer_row)
    return answer