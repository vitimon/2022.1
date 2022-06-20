def filterOnes(x):
    return x if x!= 1 else ""

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
        resultList += coefficient*(-1)
    return resultList

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
        self.coefficients = coefficients
        self.dimensions = len(coefficients) - 1
    
    def __neg__(self):
        self.coefficients = negativeList(self.coefficients)

    def __add__(self,other):
        return Polynomial(mergeLists(self.coefficients,other.coefficients))
    
    def __sub__(self,other):
        return self - other
    
    def __str__(self):
        if self.coefficients == [0]: return "0"
        stringfyed = ""
        if self.coefficients[0]: stringfyed += "{} ".format(self.coefficients[0])
        for index in range(1,self.dimensions + 1):
            if self.coefficients[index] != 0:
                stringfyed += "{} {}x{} ".format("+" if self.coefficients[index] > 0 else "-",filterOnes(self.coefficients[index]),get_super(str(index)))
        return stringfyed if self.coefficients[0] else stringfyed[2:]