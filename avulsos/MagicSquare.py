def isSquareMatrix(candidate):
    lines = len(candidate)
    for i in candidate:
        if len(i) != lines:
            return False
    return candidate, lines

def isMagicMatrix(candidate):
    candidate = isSquareMatrix(candidate)
    if candidate:
        lines = candidate[1]
        sumStraightDiagonal = 0
        sumCounterDiagonal = 0
        columnAndLineSum = None
        for i in range(lines):
            currentLineSum = 0
            currentColumSum = 0
            for j in range(lines):
                currentLineSum += candidate[0][i][j]
                currentColumSum += candidate[0][j][i]
            if currentLineSum != currentColumSum:
                return False
            if columnAndLineSum == None:
                columnAndLineSum = currentLineSum
            elif columnAndLineSum != currentLineSum:
                return False 
            sumStraightDiagonal += candidate[0][i][i]
            sumCounterDiagonal += candidate[0][i][lines-i -1]
        if (sumStraightDiagonal != columnAndLineSum) | (sumCounterDiagonal != columnAndLineSum):
            return False
        else:
            return True
    else:
        return False


