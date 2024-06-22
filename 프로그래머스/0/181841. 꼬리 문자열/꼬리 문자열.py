def solution(str_list, ex):
    answer = ''
    
    copy = []
    
    for i in str_list:
        if ex not in i:
            copy.append(i)
            
    answer = ''.join(copy)
    
    return answer