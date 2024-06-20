def solution(my_string, index_list):
    
    array = []
    
    for i in index_list: 
        array.append(my_string[i])
    
    answer = ''.join(array)
    
    return answer