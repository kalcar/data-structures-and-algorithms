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
        
mysol = Solution()

arr = [1,2]
print(arr[1:], arr[:1])