def solution(num_list):
    answer = 0
    add = 0
    mul = 1
    
    if len(num_list) >= 11 :
        for i in num_list :
            add += i
        
        answer = add
        
    elif len(num_list) <= 10 :
        for i in num_list:
            mul *= i
            
        answer = mul
                
    return answer