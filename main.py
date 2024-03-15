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


for index in range(10):

    lowestValue = 0
    print("index1:", index)

    for index2 in range(index + 1, 10):
        print("index2",index2)