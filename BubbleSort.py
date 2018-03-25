def BubbleSort(Array):
    unsorted = True
    while unsorted:
        unsorted = False
        print(Array) #Show the Array after each pass
        for item in range(0, len(Array)-1):
            #Compare and Swap
            if Array[item] > Array[item+1]:
                temp = Array[item+1]
                Array[item+1] = Array[item]
                Array[item] = temp
                unsorted = True
        
    return Array
