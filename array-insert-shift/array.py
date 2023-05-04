def insertShiftArray(array, val):
    middle  = len(arr) //2

    if len (array ) % 2 == 0:
        arr.insert(middle , val)
    else:
        array.insert(middle , val)

    print(array)
    return array
    
insertShiftArray([42,8,15,23,42], 16)