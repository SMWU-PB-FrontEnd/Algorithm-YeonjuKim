def solution(myString):
    
    answer = myString.translate(str.maketrans('abcdefghijk','lllllllllll'))
    
    return answer