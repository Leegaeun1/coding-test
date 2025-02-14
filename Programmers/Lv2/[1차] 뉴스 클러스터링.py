def two(li_s,s):
    for i in range(0,len(s)-1):
        if s[i].isalpha() and s[i+1].isalpha():
            li_s.append(s[i:i+2])
    return li_s

def dictionary(li):
    dic={}
    for i in li:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return dic

def solution(str1, str2):
    li_s1,li_s2=[],[]
    union,inter=0,0
    str1=str1.lower()
    str2=str2.lower()
    li_s1=two(li_s1,str1) # 두글자씩 묶기
    li_s2=two(li_s2,str2)
    s1_dic=dictionary(li_s1) # 딕셔너리로 몇개인지 보기
    s2_dic=dictionary(li_s2)
    
    for i in s1_dic:
        if i in s2_dic:
            union+=max(s2_dic[i],s1_dic[i])
            inter+=min(s1_dic[i],s2_dic[i])
        else:
            union+=s1_dic[i]
    for i in s2_dic:
        if i not in s1_dic:
            union+=s2_dic[i]
    if union==0:
        return 65536
    return int(inter/union*65536)