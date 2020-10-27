def kadanesAlgorithm(array):
    maxEndingHere = array[0]
    maxSoFar = array[0]
    for val in array[1:]:
        maxEndingHere = max(val, maxEndingHere + val)
        maxSoFar = max(maxSoFar, maxEndingHere)
    return maxSoFar

test = [3,5,-9,1,3,-2,3,4,7,2,-9,6,3,1,-5,4]
print(kadanesAlgorithm(test) == 19)