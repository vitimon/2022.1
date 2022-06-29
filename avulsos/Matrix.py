from ast import Return
from pickle import EMPTY_DICT
from time import sleep
from random import randint
from os import system

clear = lambda: system('clear')

class Matrix:
    matrix = []
    lines = 0
    columns = 0
    def __init__(self,n,m,v):
        self.lines = n
        self.columns = m
        self.matrix = []
        for line in range(self.lines):
            self.matrix += [[]]
            for column in range(self.columns):
                self.matrix[line] += [v[line][column]]

    """def __init__(self,lines,columns,**initializers):
        self = Matrix(lines,columns,[[0]*columns]*lines)"""

    def __add__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be added.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] + other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)

    def __sub__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be subtracted.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] - other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)


    def __mul__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be multiplied.")
        if (self.lines != other.columns) | (self.columns != other.lines):
            raise("Matrixes must be multiplicable: (LinesA = ColumnsB) & (ColumnsA = LinesB).")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(other.columns):
                element = 0
                for stack in range(self.columns):
                    element += self.matrix[line][stack]*other.matrix[stack][column]
                result[line] += [element]
        return Matrix(self.lines,other.columns, result)

    def __or__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be 'ored'.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] | other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)
    
    def __xor__(self,other):
        if type(self) != type(other):
            raise("Only matrixes can be 'xored'.")
        if (self.lines != other.lines) | (self.columns != other.columns):
            raise("Matrixes must have the same number of lines and columns.")
        result = []
        for line in range(self.lines):
            result += [[]]
            for column in range(self.columns):
                result[line] += [self.matrix[line][column] ^ other.matrix[line][column]]
        return Matrix(self.lines,self.columns, result)

    def __str__(self):
        stringfyed = ""
        for line in self.matrix:
            stringfyed += str(line) + "\n"
        return stringfyed
    
    def __filterCell(self,x,y,pattern = [0]):
        size = len(pattern)
        if y < -1:
            raise("Y OUT OF LESSER BOUNDARIES")
        if y > self.lines:
            raise("Y OUT OF UPPER BOUNDARIES")
        if x < -1:
            raise("X OUT OF LEFTMOST BOUNDARIES")
        if x > self.columns:
            raise("X OUT OF RIGHTMOST BOUNDARIES")
        if y == -1:
            return pattern[(x+1)%size]
        if x == self.columns:
            return pattern[(self.columns + y + 2 )%size]
        if y == self.lines:
            return pattern[(2*self.columns + self.lines -x + 2)%size ]
        if x == -1:
            return pattern[(2*self.columns + 2*self.lines - y + 3)%size]
        return 1 if self.matrix[y][x] > 0 else 0

    def __cellquence(self,x,y,externalPattern =[0]):
        currentState = self.matrix[y][x]
        nextState = 0
        lives = False
        for delta1 in range(-1,2):
            for delta2 in range(-1,2):
                nextState += self.__filterCell(x+delta1,y+delta2, externalPattern)
        if (nextState == 3) | (nextState - currentState) == 3: lives = True
        #print("cell: {},{} ---- sum: {}, current: {}  so it lives? {}".format(x,y,nextState,currentState,lives))
        return 1 if (nextState == 3) | (nextState - currentState) == 3 else 0



    def nextState(self,borderPattern =[0]):
        nextMatrix = []
        for line in range(self.lines):
            nextMatrix+= [[]]
            for column in range(self.columns):
                nextMatrix[line] += [ self.__cellquence(column,line,borderPattern) ]
        return Matrix(self.lines,self.columns,nextMatrix)
    
    def simulateCGoL(self,steps = 1,timer = 1,pattern = [0]):
        print(self)
        simulated = self.nextState(pattern)
        while(steps > 0):
            if simulated.matrix == simulated.lines*[simulated.columns*[0]]: return "DIED before {} steps completion".format(steps)
            print(steps)
            print(simulated)
            simulated = simulated.nextState(pattern)
            steps -= 1
            sleep(timer)
            clear()
        return "final matrix:\n{}".format(simulated)

    def insertBlock(self,x,y):
        if (x > self.columns - 2): raise("OUT OF BOUNDS")
        if (y > self.lines - 2): raise("OUT OF BOUNDS")
        if (x < 0): raise("OUT OF BOUNDS")
        if (x < 0): raise("OUT OF BOUNDS")
        self.matrix[y][x] = 1
        self.matrix[y + 1][x] = 1
        self.matrix[y][x + 1] = 1
        self.matrix[y + 1][x + 1] = 1
        return self

def makeEmptyMatrix(lines,columns):
    return Matrix(lines,columns,[[0]*columns]*lines)

def makeFullMatrix(lines,columns):
    return Matrix(lines,columns,[[1]*columns]*lines)


def makeRandomBinaryMatrix(lines,columns):
    binaryMatrix = []
    for line in range(lines):
        binaryMatrix += [[]]
        for column in range(columns):
            binaryMatrix[line] += [randint(0,1)]
    return Matrix(lines,columns,binaryMatrix)

def makeRandomPattern(lines,columns):
    randomPattern = []
    for element in range(2*lines + 2*columns + 4):
        randomPattern += [randint(0,1)]
    return randomPattern

def simulateRandom(size):
    initialState = makeRandomBinaryMatrix(size,size)
    initialState.simulateCGoL(100,1)
