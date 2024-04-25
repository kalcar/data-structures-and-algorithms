# code goes here.

myArray = [1, 4, 9, 12, 15, 20, 24] # 7 items

myArray2 = [1, 4, 9, 12, 15, 20, 24, 49] # 8 items

#len = 7 or 8
# print(len(myArray), len(myArray2), len(myArray) >> 1, len(myArray2) >> 1)

# print(bin(7), bin(1))
# check to see if the "1" value bit is set in the int
# if its 0, then that bit isnt set. 
# print(7 & (1 << 0))


print(len(myArray)) # 7
resizeT = 10

extra = 10 - len(myArray)

extral = [None]*extra

myArray.extend(extral)
print(myArray, len(myArray))

resizeT = 5

remove = len(myArray) - 5

myArray = myArray[:resizeT]
print(myArray, len(myArray))
myArray.clear()
print(myArray)

# print(1 >> 1)





# leetcode hard question practice
# TODO: make a "smart join"
# TODO: use indexes instead of slices


# in both arrays, compare the medians to eachother
def isEven(num: int):
    if num == 0: # 0 is neither even or odd
        return None
    
    if (num & 0b1 == 1):
        return False
    else:
        return True
    

def findMedian(arr):
    if (isEven(len(arr))):
        index = (len(arr) >> 1) - 1
        return (arr[index + 1] + arr[index])/2 , index
    else:
        index = len(arr) >> 1
        return arr[index], index 

doprint = True
def cprint(*args, **kwargs):
    if doprint:
        print(*args, **kwargs)


def recursiveMedianJoin(arr1, arr2):


    if len(arr2) == 0:
        return arr1
    
    while ((len(arr1) > 1) and (len(arr2) > 1)): # while theres multiple items in the arrays
        arr1Median, arr1Index = findMedian(arr1)
        arr2Median, arr2Index = findMedian(arr2)



        cprint("array1, median, and index: ", arr1, "median:", arr1Median, "index:", arr1Index, len(arr1) )
        cprint("array2, median, and index: ", arr2, "median:", arr2Median, "index:", arr2Index, len(arr2) )
        # make sure arr1 is bigger
        if len(arr1) < len(arr2):
            return recursiveMedianJoin(arr2, arr1)

        # compare medians
        if arr1Median == arr2Median:
            # if the medians are the same, then merge the two and return. Best case

            combinedArray = arr2[:arr2Index + 1] + arr1 + arr2[arr2Index + 1:]
            return combinedArray
        elif arr1Median > arr2Median:
            # combine the arrays where the median is in a known half
            cprint("Heres the chunk going at the beginning of arr1: ", arr2[:arr2Index+1], "\n")
            # join based on the highest value
            cprint("matching the lowest value:", arr1[arr1Index-1], arr2[arr2Index])
            if arr1[arr1Index-1] > arr2[arr2Index-1]:
                combinedArray = arr2[:arr2Index +1] + arr1
                
                cprint("combining:", arr2[:arr2Index +1] , arr1)

            elif arr1[arr1Index-1] < arr2[arr2Index-1]:

                cprint("combining:", arr1[:arr1Index] , arr2[:arr2Index +1] , arr1[arr1Index:])
                combinedArray = arr1[:arr1Index] + arr2[:arr2Index +1] + arr1[arr1Index:]
            else:
                combinedArray = arr2[:arr2Index +1] + arr1
            # the "search" median is now in the lower half of array 1, or in the lower half of array 2

            return recursiveMedianJoin(combinedArray, arr2[arr2Index+1:])
            # do the same again, with the leftover array

        elif arr1Median < arr2Median:
            cprint("Heres the chunk going at the end of arr1: ", arr2[arr2Index + 1 :], "\n")

            cprint("matching the lowest value:", arr1[arr1Index + 1] , arr2[arr2Index + 1])
            # want the lowest to touch the median
            if arr1[arr1Index + 1] < arr2[arr2Index + 1]:
                cprint("combining: ", arr1 , arr2[arr2Index + 1:])
                combinedArray = arr1 + arr2[arr2Index + 1:]

            elif arr1[arr1Index + 1] > arr2[arr2Index + 1]:
                cprint("combining: ", arr1[:arr1Index +1] , arr2[arr2Index+1:] , arr1[arr1Index+1:])
                combinedArray = arr1[:arr1Index +1] + arr2[arr2Index+1:] + arr1[arr1Index+1:]
            else:
                combinedArray = arr1 + arr2[arr2Index + 1:]

            # the "search" median is now in the upper half array 1, or in the upper half of array 2

            return recursiveMedianJoin(combinedArray, arr2[:arr2Index + 1])
            # do the same again, with the leftover array
    
    median , index = (findMedian(arr1))

    cprint("single element time", arr1, arr2)

    if median > arr2[0]: # going to the front
        if arr2[0] > arr1[index - 1]:
            return arr1[:index+1] + arr2 + arr1[index+1:]

        return arr2 + arr1
        
    
    elif median < arr2[0]: # going to the back

        if arr2[0] < arr1[index + 1]:

            return arr1[:index + 1] + arr2 + arr1[index + 1:]
        
        return arr1 + arr2
    
    elif median == arr2[0]:
        # print(arr1[:index+1] , arr2 , arr1[index+1:])
        return arr1[:index+1] + arr2 + arr1[index+1:]


def recursiveMedianSearch(arr1, arr2, high1, low1, high2, low2):
    if len(arr1) < len(arr2):
        recursiveMedianSearch(arr2, arr1, high2, low2, high1, low1)
    
    while len(arr2) > 1: # while there are 2 or more items in array 2
        # find the median of both arrays
        arrmedian1 = 0
        arrmedian2 = 0

        if arrmedian2 == arrmedian1:
            return arrmedian1

        if arrmedian1 > arrmedian2:
            pass

        elif arrmedian1 < arrmedian2:
            pass







arr1 =  [3, 50, 81]
arr2 = [2, 36, 45]




newarr = recursiveMedianJoin(arr1, arr2)
print(newarr, findMedian(newarr))
newarr.sort()
print(newarr)

newarr = arr1 + arr2
newarr.sort()
print(newarr, findMedian(newarr) )

import random


def runTrials(trials):

    for i in range(trials):
        
        arr1 = []
        arr2 = []

        number = random.random()*2+2

        for j in range(int(number)):
            arr1.append(int(random.random()*100))

        number = random.random()*2+2
        for j in range(int(number)):
            arr2.append(int(random.random()*100))

        arr1.sort()
        arr2.sort()

        resultarr = recursiveMedianJoin(arr1,arr2)
        resultmedian, z = findMedian(resultarr)

        checkarr = arr1 + arr2
        checkarr.sort()
        checkmedian, z = findMedian(checkarr)
        print("input:", arr1, arr2)
        print("Trial:", resultarr, resultmedian)
        print("result median:",checkarr, checkmedian, "pass?", resultmedian == checkmedian)
    
# runTrials(100)
    

