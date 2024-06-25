def solution(my_strings, parts):
    answer = ''
    arr = []
    
    for i in range(0, len(parts)):
        s = parts[i][0]
        e = parts[i][1]
        
        arr.append(my_strings[i][s:e+1])
        
    answer = ''.join(arr)
    
    return answer