def solution(num_list, n):
    answer = []
    front = []
    back = []
    
    for i in range(0,len(num_list)):
        if i <= n-1 : front.append(num_list[i])
        else : back.append(num_list[i])
        
    back.extend(front)
    answer = back
        
    return answer