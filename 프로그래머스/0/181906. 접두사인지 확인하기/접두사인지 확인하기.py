def solution(my_string, is_prefix):
    answer = 0
    string = ''
    arr = []
    
    for i in range(0, len(my_string)) :
        string += my_string[i]
        arr.append(string)
    print(arr)
        
    for j in arr :
        print(is_prefix, j)
        if is_prefix == j : return 1
        else : answer = 0
    
    return answer