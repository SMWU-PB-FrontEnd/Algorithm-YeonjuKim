def solution(n, control):
    
    temp = n
    
    print(temp)
    
    for i in range(0, len(control)):
        j = control[i]
        if (j == "w") : temp += 1   
        elif (j == "s") : temp -= 1  
        elif (j == "d") : temp += 10   
        elif (j == "a") : temp -= 10   
        
    answer = temp
    
    return answer