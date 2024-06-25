def solution(myString):
    answer = ''
    arr = []
    
    lowerString = myString.lower()
    
    for i in range(0, len(lowerString)) :
        if lowerString[i] == "a" : 
            arr.append(lowerString[i].upper())
        else : arr.append(lowerString[i])
    
    answer = ''.join(arr)
    
        
    return answer