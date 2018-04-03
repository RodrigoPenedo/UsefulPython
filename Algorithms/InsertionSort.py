def InsertionSort(array):
    for i in range(1, len(array)):
 
        current = array[i]
        number = i-1
        
        while number >=0 and current < array[number] :
                array[number+1] = array[number]
                number -= 1
                
        array[number+1] = current

        #print(array)

    return array


array = [20, 21, 30, 7, 19, 10, 5]
print(InsertionSort(array))

