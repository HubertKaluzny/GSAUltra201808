import math

def solution(a):
    almostSquares = 0
    for i in range(10, a + 1):
        if(isAlmostSquare(i)):
            almostSquares += 1
    return almostSquares

def isAlmostSquare(i):
    iStr = str(i)
    for x in range(0, len(iStr)):
        sub = iStr[:x] + iStr[x + 1:]
        intSub = int(sub)
        if math.sqrt(intSub).is_integer():
            return True
        elif intSub == 0:
            return True

    return False 
