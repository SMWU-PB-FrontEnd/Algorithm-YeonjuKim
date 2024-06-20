def solution(my_string, overwrite_string, s):
    
    length = len(overwrite_string)
    
    old = my_string[s:s+length]
    
    answer = my_string[:s] + overwrite_string + my_string[s+length:]
    
    return answer