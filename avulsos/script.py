matrixInput = input('Digite uma matriz.')
#checando ---- no lugar nos prints se usaria um return em caso de funções
opens = 0
closes = 0
result = []
currentLine=[]
currentCell = 0
for i in matrixInput:
    if (i == '['):
        opens += 1
        if (opens - closes > 2):
            print('apenas 2 dimensões pfv')
    elif(i == ']'):
        closes += 1
        if (closes == opens):
            print(result)
        currentLine += [currentCell]
        currentCell = 0
        result += [currentLine]
        currentLine = []
    elif((i == ',') & ((opens - closes) > 1)):
        currentLine += [currentCell]
        currentCell = 0
    elif(i != ','):
        currentCell = currentCell*10 + int(i)
        
    