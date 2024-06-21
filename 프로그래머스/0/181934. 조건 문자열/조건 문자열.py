def solution(ineq, eq, n, m):
    
    con = ineq + eq
    
    answer = 0
    
    if (n>=m and con == '>=') : answer = 1
    elif (n<=m and con == '<=') : answer = 1 
    elif (n>m and con == '>!') : answer = 1
    elif (n<m and con == '<!' ) : answer = 1
    else : answer = 0

    return answer