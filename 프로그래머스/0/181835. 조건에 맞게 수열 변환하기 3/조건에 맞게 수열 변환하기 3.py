def solution(arr, k):
    answer = []
    restK = k%2
    
    if (restK == 1) :
        for i in arr :
            answer.append(i*k)
    else : 
        for i in arr :
            answer.append(i+k)
    
    return answer