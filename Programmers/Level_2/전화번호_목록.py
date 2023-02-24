from collections import defaultdict

def solution(phone_book):
    
    store = {}

    for i in range(len(phone_book)):
        store[phone_book[i]] = i
    
    for phone_num in phone_book:
        str = ''
        for num in phone_num:
            str += num
            if str != phone_num and str in store:
                return False
            
    return True
