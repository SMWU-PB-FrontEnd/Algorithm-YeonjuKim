def solution(str1, str2):
    
    arr = []
    
    for i in range(0,len(str1)):
        arr.append(str1[i])
        arr.append(str2[i])
        
    answer = ''.join(arr)
    return answer