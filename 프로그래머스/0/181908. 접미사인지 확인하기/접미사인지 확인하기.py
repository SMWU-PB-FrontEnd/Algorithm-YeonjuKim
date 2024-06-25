def solution(my_string, is_suffix):
    answer = 0
    arr = []
    
    for i in range(0, len(my_string)) :
        arr.append(my_string[i+1:])
    
    arr.append(my_string)
    
    if is_suffix in arr :
        answer = 1
        
    return answer