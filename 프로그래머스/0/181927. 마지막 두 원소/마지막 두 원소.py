def solution(num_list):
    
    last = num_list[-1]
    prevLast = num_list[-2]
    
    if (last > prevLast) :
        num_list.append(last-prevLast)
    else :
        num_list.append(last*2)
        
    answer = num_list
    return answer