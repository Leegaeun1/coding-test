def solution(phone_book):
    phone_book.sort()
    n=0
    i=n+1
    while(n<len(phone_book)-1):

        if(phone_book[i][:len(phone_book[n])]==phone_book[n]):
                return False
        else:
            break
        n+=1
        i+=1
        if i>=len(phone_book):
            i=n+1
        
    return True