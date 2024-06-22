def solution(arr, n):
    answer = []
    
    restLen = len(arr)%2
    
    if (restLen == 1) :
        for i in range(0,len(arr)) :
            if (i%2 == 0) :
                answer.append(arr[i]+n)
            else : answer.append(arr[i])
    else : 
        for i in range(0,len(arr)) : 
            if (i%2 == 1) :
                answer.append(arr[i]+n)
            else :
                answer.append(arr[i])
    return answer