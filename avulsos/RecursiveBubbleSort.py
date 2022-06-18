def recursiveBubbleSort(unorderedList):
    pivot = unorderedList[0]
    if len(unorderedList) <= 1: return unorderedList
    pivot = unorderedList[0]
    for i in unorderedList[1:]: 
        if i < pivot: pivot = i 
    unorderedList.remove(pivot)
    return [pivot] + recursiveBubbleSort(unorderedList)

    