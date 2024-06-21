def solution(num_list):
    
    mul = 1
    add = 0
    
    for i in num_list :
        mul *= i
        add += i
        
    answer = 0
    
    
    if (mul < add**2) : answer = 1
    elif (mul > add**2) : answer = 0
    
    return answer