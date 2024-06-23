def solution(numLog):
    answer = ''
    arr = []
    
    for i in range(1,len(numLog)) :
        
        if (numLog[i-1] +1 == numLog[i]) :
            arr.append("w")
        elif (numLog[i-1] -1 == numLog[i]) :
            arr.append("s")
        elif (numLog[i-1] +10 == numLog[i]) :
            arr.append("d")
        elif (numLog[i-1] -10 == numLog[i]) :
            arr.append("a")
    
    answer = ''.join(arr)
           
    return answer