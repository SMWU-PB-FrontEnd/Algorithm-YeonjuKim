def solution(a, d, included):
    answer = 0
    arr = []
    
    print(len(included))
    
    for i in range(0,len(included)) :
        arr.append(a + d * i)
        
        if (included[i] == True) :
            answer += a + d * i

    print(answer)
        
    return answer