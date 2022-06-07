def recursiveBubbleSort(unorderedList, orderedList = []):
    pivot = unorderedList[0]
    #DESANINHAR IFS
    if len(unorderedList) > 1:
        for i in unorderedList[1:]:
            if i < pivot:
                pivot = i 
    unorderedList.remove(pivot)
    return recursiveBubbleSort(unorderedList, orderedList + [pivot]) if unorderedList else orderedList + [pivot]

    