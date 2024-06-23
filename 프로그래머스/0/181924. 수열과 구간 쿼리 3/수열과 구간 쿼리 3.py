def solution(arr, queries):
    answer = arr
    
    for q in queries :
        q0 = q[0]
        q1 = q[1]
        
        answer[q0],answer[q1] = answer[q1],answer[q0]
    
    return answer