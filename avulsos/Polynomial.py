from math import fabs

def filterFloat(num):
    return num if int(num) != num else int(num)

def filterOnesAndSignals(x):
    return fabs(x) if (x != 1) | (x != -1) else ""

def mergeLists(list1,list2):
        lenght1,lenght2 = len(list1),len(list2)
        minLenght = min(lenght1,lenght2)
        result = []
        for sum in range(minLenght):
            result += [list1[sum]+list2[sum]]
        return result + list1[minLenght:] if lenght1 >= lenght2 else result + list2[minLenght:]

def negativeList(list):
    resultList =[]
    for coefficient in list:
        resultList += [coefficient*(-1)]
    return resultList

def trimRightmostZeroes(list):
    return list if ((list[-1] != 0) | (len(list) == 1)) else trimRightmostZeroes(list[0:-1])

def getLeftmostNonZero(list):
    return list[0] if (list[0] != 0) | (list == [0]) else getLeftmostNonZero(list[1:])

def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)

class Polynomial:
    def __mergeLists(list1,list2):
        lenght1,lenght2 = len(list1),len(list2)
        minLenght = min(lenght1,lenght2)
        result = []
        for sum in range(minLenght):
            result += [list1[sum]+list2[sum]]
        return result + list1[minLenght:] if lenght1 >= lenght2 else result + list2[minLenght:]

    def __init__(self,coefficients=[0]):
        self.coefficients = trimRightmostZeroes(coefficients)
        self.degree = len(self.coefficients) - 1
    
    def __getitem__(self,degree):
        return self.coefficients[degree] if self.degree >= degree else 0

    def __setitem__(self, degree, coefficient):
        if self.degree < degree:
            currentDegree = self.degree
            self.degree = degree
            self.coefficients = self.coefficients + [0]*(degree - currentDegree -1) +[1]
        else:
            self.coefficients[degree] = coefficient
    
    def __neg__(self):
        return Polynomial(negativeList(self.coefficients))

    def __add__(self,other):
        return Polynomial(mergeLists(self.coefficients,other.coefficients))
    
    def __sub__(self,other):
        return Polynomial(mergeLists(self.coefficients,negativeList(other.coefficients)))
    
    def __mul__(self,other):
        result = [0]*(self.degree + other.degree + 1)
        for index1 in range(self.degree + 1):
            if self.coefficients[index1]:
                for index2 in range(other.degree + 1):
                    if other.coefficients[index2]:
                        result[index1 + index2] += self.coefficients[index1]*other.coefficients[index2]
        return Polynomial(result)

    def __pow__(self,exp):
        if exp == 0: return Polynomial([1])
        return self*(self**(exp-1)) if exp > 1 else self

    def __mod__(self,other):
        return (self - other*Polynomial([0]*(self.degree - other.degree) + [self.coefficients[-1]/other.coefficients[-1]]))%other if self.degree >= other.degree else self

    def __floordiv__(self,other):
        return Polynomial([0]*(self.degree - other.degree) + [self.coefficients[-1]/other.coefficients[-1]]) + (self - other*Polynomial([0]*(self.degree - other.degree) + [self.coefficients[-1]/other.coefficients[-1]]))//other if self.degree >= other.degree else Polynomial()

    def isRoot(self,num):
        return False if (self%Polynomial([(-1)*num,1])).coefficients != [0] else True

    def __str__(self):
        if self.coefficients == [0]: return "0"
        stringfyed = ""
        if self.coefficients[0]: stringfyed += "{} ".format(self.coefficients[0])
        for index in range(1,self.degree + 1):
            if self.coefficients[index] != 0:
                stringfyed += "{} {}x{} ".format("+" if self.coefficients[index] > 0 else "-",filterFloat(filterOnesAndSignals(self.coefficients[index])),get_super(str(index)))
        if ((self.coefficients[0] == 0) & (getLeftmostNonZero(self.coefficients) < 0)): stringfyed = "--"+stringfyed
        return stringfyed if self.coefficients[0] else stringfyed[2:]

    def evaluate(self,x):
        result = 0
        coefficients = self.coefficients
        for degree in range(self.degree + 1):
            result += coefficients[degree]*(x**degree)
        return(result)

    def evaluate2(self,x):
        return self%Polynomial([(-1)*x,1])

    def derivate(self):
        coefficients = self.coefficients
        if len(coefficients) > 1: coefficients.pop(0)
        else: return 0
        result = Polynomial(coefficients)
        for degree in range(1, result.degree + 1):
            result[degree] = coefficients[degree]*(degree + 1)
        return result
    
    def compose(self,other):
        composition = Polynomial([0])
        for degree in range(self.degree + 1):
            if self.coefficients[degree]: composition += (Polynomial([self.coefficients[degree]])*(other**degree))
        return composition
        

def makePolynomialFromRoots(roots = [0], multiplyer = 1):
    if len(roots) < 2: return Polynomial([roots[0],1])*Polynomial([multiplyer])
    return makePolynomialFromRoots(roots[1:]) * Polynomial([(-1)*roots[0],1]) if len(roots) > 2 else Polynomial([multiplyer])*Polynomial([(-1)*roots[0],1])*Polynomial([(-1)*roots[1],1])