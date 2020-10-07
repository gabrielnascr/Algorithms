def binarysearch(array, value, begin=0):
    end = len(array)-1

    while (begin <= end):
        middle = (begin + end)//2
        if value > array[middle]:
            begin = middle + 1
        if value < array[middle]:
            end = middle - 1
        else:
            return middle

    return None


array = [8,1,7,2,3]

result = binarysearch(array, 8)

if result == None:
    print('The value was not found')
else:
    print('The value was found in the index {:d}'.format(result))
