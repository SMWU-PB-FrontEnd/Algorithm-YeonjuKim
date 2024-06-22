def solution(arr1, arr2):
    answer = 0
    sum1 = 0
    sum2 = 0
    
    len1 = len(arr1)
    len2 = len(arr2)
    
    for i in arr1 :
        sum1 += i
        
    for i in arr2 :
        sum2 += i
    
    if (len1 == len2):
        if (sum1>sum2): answer = 1
        elif(sum2>sum1): answer = -1
        else : answer = 0
    else :
        if (len1>len2) : answer = 1
        elif(len2>len1): answer = -1
        else : answer = 0
    
    return answer