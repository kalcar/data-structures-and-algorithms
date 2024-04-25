class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        median = self.findMedian(self.recursiveMedianJoin(nums1, nums2))
        return median[0]


    
    def isEven(self, num):
        if num == 0: # 0 is neither even or odd
            return None
        
        if (num & 0b1 == 1):
            return False
        else:
            return True

    def findMedian(self, arr):
        if (self.isEven(len(arr))):
            index = (int(len(arr) /2)) - 1
            return (arr[index + 1] + arr[index])/2 , index
        else:
            index = int(len(arr) /2)
            return arr[index], index 

        
    def recursiveMedianJoin(self, arr1, arr2):

        arr1Median, arr1Index = self.findMedian(arr1)
        arr2Median, arr2Index = self.findMedian(arr2)

        while ((len(arr1) > 1) and (len(arr2) > 1)): # while theres multiple items in the arrays
            
            # compare medians
            if arr1Median == arr2Median:
                # if the medians are the same, then merge the two and return. Best case

                combinedArray = arr2[:arr2Index + 1] + arr1 + arr2[arr2Index + 1:] # why is this off by 1?
                return combinedArray
            elif arr1Median > arr2Median:
                # combine the arrays where the median is in a known half
               
                combinedArray = arr2[:arr2Index] + arr1
                # the "search" median is now in the lower half of array 1, or in the lower half of array 2

                return self.recursiveMedianJoin(combinedArray, arr2[arr2Index:])
                # do the same again, with the leftover array

            elif arr1Median < arr2Median:
                
                combinedArray = arr1 + arr2[arr2Index + 1:]
                # the "search" median is now in the upper half array 1, or in the upper half of array 2

                return self.recursiveMedianJoin(combinedArray, arr2[:arr2Index + 1])
                # do the same again, with the leftover array
            
        median , index = (self.findMedian(arr1))

        if median > arr2[0]:
            return arr2 + arr1
        
        elif median < arr2[0]:
            return arr1[:index+1] + arr2 + arr1[index+1:]
        
        elif median == arr2[0]:
            return arr1[:index+1] + arr2 + arr1[index+1:]
        
# If statement so I can collapse this particular test case or run it when I want to
solution = False
if solution:

    mysol = Solution()

    arr = [1,2]
    print(arr[1:], arr[:1])


my_bytes = bytearray('mystring321', encoding='UTF8')
print(my_bytes)
mv = memoryview(my_bytes)
print(mv[0])
for byte in mv:
    print(format(byte, "b"))

# how many bits are needed to store an integar
def intToBits(myint):
    # format the int as a binary, and return the length of the resulting string
    return len(format(myint, "b"))

def concatBits(byte1, byte2):
# shift to the left the number of bits byte2 is, then bitwise OR them to combine
    return ((byte1 << intToBits(byte2)) | byte2)

# concat all the bytes together
binary = 0
for byte in mv:
    binary = concatBits(byte, binary)

print(format(binary,"b"))
print(type(binary))


# for a given number of bits, continuously XOR the entire binary sequence until the length is shorter than the number
desiredbits = 5


# this is a bad, wasteful method. OH WELL
binString = format(binary, "b")


hashed = 0
sliceStart = len(binString) -5
sliceEnd = len(binString)


while sliceStart >= 0:
# note: negative indices dont make this easier
    working = binString[sliceStart:sliceEnd]
    print(working, sliceStart, sliceEnd)
    
    # make sure both are ints so bitwise XOR works
    working = int(working, 2)
    hashed = hashed ^ working

    sliceEnd = sliceStart
    sliceStart -= desiredbits
    print(format(hashed, "b"))

print(hashed)


