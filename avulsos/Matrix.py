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
                for sum in range(self.columns):
                    element += self.matrix[line][sum]*other.matrix[sum][column]
                result[line] += [element]
        return Matrix(self.lines,other.columns, result)

    def __repr__(self):
        return str(self.matrix())