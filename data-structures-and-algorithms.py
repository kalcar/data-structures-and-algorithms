# TODO: implement this later <- probably never going to be done tbh
class MemError(Exception):
    pass

class Memory():
    def __init__(self, memsize: int):

        # initalize an empty list with N "addresses"
        self.memoryAddresses = [None]*memsize
        self.operations = 0
        self.size = memsize

    def getList(self):
        return self.memoryAddresses
    
    def getOperations(self):
        return self.operations
    
    def getSize(self):
        return self.size

    # put a list into memory
    def loadList(self, list):
        if not (len(list) == len(self.memoryAddresses)):
            raise MemError
        else:
            for index in range(len(list)):
                self.memoryAddresses[index] = list[index]
    
    # resize memory, deleting values if the new size is smaller than current
    def resizeMemory(self, size):
        """ Resizes the internal list, the 'addresses'

            Args: 
                size (int): non-negative, desired size of memory

            Returns: 
                Nothing

            Raises: 
                Memerror if size is negative
        """
        if size < 0:
            raise MemError

        if size > self.size:
            # create an empty list with the desired number of extra elements
            expandList = [None]*(size - len(self.memoryAddresses))
            # extend the current list
            self.memoryAddresses.extend(expandList)

        elif size < self.size:
            # reassign the variable with the desired, reduced length
            self.memoryAddresses = self.memoryAddresses[:size]

        self.size = size
    
    def resetOperations(self):
        self.operations = 0

    def clearMemory(self):
        self.memoryAddresses.clear()
        self.operations = 0
        self.size = 0
    
    def read(self, index):
        self.operations += 1
        return self.memoryAddresses[index]
    
    def insert(self, index, value):
        # move over all items in the array by 1 space, then insert the item into the index
        self.operations += len(self.memoryAddresses) - index + 2 
        # +1 to convert index into element number, then +1 for the actual insertion

        self.memoryAddresses.insert(index, value)
    
    def delete(self, index):
        # delete, then move all items in array by 1 space
        self.operations += len(self.memoryAddresses) - index + 1
        # +1 to convert index to element number, +1 for the deletion, but -1 because there's 1 fewer element in the list
        self.memoryAddresses.pop(index)

    def compare(self, index1, index2, operator):
        self.operations += 1
        match operator:
            case "<":
                return self.memoryAddresses[index1] < self.memoryAddresses[index2]
            case "<=":
                return self.memoryAddresses[index1] <= self.memoryAddresses[index2]
            case ">":
                return self.memoryAddresses[index1] > self.memoryAddresses[index2]
            case ">=":
                return self.memoryAddresses[index1] >= self.memoryAddresses[index2]
            case "==":
                return self.memoryAddresses[index1] == self.memoryAddresses[index2]
            case "!=":
                return self.memoryAddresses[index1] != self.memoryAddresses[index2]
            case _:
                raise MemError
            
        
    
    def swap(self, index1, index2):
        self.operations += 1
        # store both values
        tempVal = self.memoryAddresses[index1]
        tempVal2 = self.memoryAddresses[index2]
        # assign the values to opposing indices
        self.memoryAddresses[index1] = tempVal2
        self.memoryAddresses[index2] = tempVal

def linearSearch(memory: Memory, value):
    """
    conducts a linear search on the custom class 'memory'

    Args:
        memory (Memory): the custom class that simulates computer memory
        value (any literal): the target value the algorithm is searching for
    
    Returns:
        int: the index of the search target
        None: if the search target does not exist in memory

    Raises:
        Nothing

    """
    # loop over memory, reading each value
    for index in range(memory.getSize()):
        # return the index when a match is found
        if value == memory.read(index):
            return index

def binarySearch(memory: Memory, upperBound: int, lowerBound: int, value):
    """
    conducts a binary search on the custom class 'memory'. upperbound and Lowerbound is for the sake of recursion

    Args:
        memory (Memory): the custom class that simulates computer memory
        upperBound (int): the index of the upper limit of the search area
        lowerBound (int): the index of the lower limit of the search area
        value (any literal): the target value the algorithm is searching for
    
    Returns:
        int: the index of the search target
        None: if the search target does not exist in memory

    Raises:
        Nothing

    """
    # find the middle index of the array, always rounding down!
    middle = lowerBound + ((upperBound - lowerBound) >> 1)

    # read the middle value, set search area to be the upper or lower segment based on if the value is found to be higher or lower
    middleValue = memory.read(middle)

    # check to see if the middle value is the search value. return it if found
    if middleValue == value:
        return middle
    
    # if the search space is exhausted. This occurs when the search space is 1 element and final possible value was evaluated (the value is evaluated in the if block directly above)
    elif lowerBound == upperBound:
        return None # Exit the search, value not found in array
    
    # if the search space has 2 elements, the lower bound is equal to the middle since the algorithm rounds down.
    elif lowerBound == middle: # this happens if the search reaches the edge of the list, when lower and upper are within 1
        lowerBound = upperBound # do one last search (search space has 1 element, see above elif)
        print("reached edge of search space. Final loop")
        return binarySearch(memory, upperBound, lowerBound, value) # call the search again with the new boundaries

    # set the lower bounds to the middle index if the value exists within the upper half of the search space
    elif middleValue < value:
        lowerBound = middle
        return binarySearch(memory, upperBound, lowerBound, value) # call the search again with the new boundaries

    # set the upper bounds to the middle index if the value exists within the lower half of the search space
    elif middleValue > value:
        upperBound = middle
        return binarySearch(memory, upperBound, lowerBound, value) # call the search again with the new boundaries 

def bubbleSort(memory: Memory):
    """
    sorts the internal list in ascending order the custom class 'memory'

    Args:
        memory (Memory): the custom class that simulates computer memory
    
    Returns:
        list (list): the sorted list

    Raises:
        Nothing

    """
    # assuming the list is unsorted
    sorted = False

    # the index where the list is in correct order until the end. -1 to make sure the index stays within range
    sortedUntil = memory.getSize() - 1

    # loop through the sort until its sorted
    while sorted == False:
        # until a swap is made, we can assume its sorted. A loop with no swaps is sorted
        sorted = True

        # go through every value, moving the largest value forward to the end
        for index in range(sortedUntil):

            # compare if the next value is smaller than the previous, if so swap them
            if memory.compare(index, index + 1, ">"):
                sorted = False # if a swap is made, the list isnt sorted
                memory.swap(index, index + 1)

        # decrement sortedUntil since the loop just confirmed a sorted element at the largest index
        sortedUntil -= 1
    
    return memory.getList()      
        
def hasDuplicates(memory: Memory):
    """
    determines if the internal list of the memory class has duplicates

    Args:
        memory (Memory): the custom class that simulates computer memory
    
    Returns:
        bool: True if duplicates exist, False if each element is unique

    Raises:
        Nothing

    """
    items = {} # values of the list are keys, num occurances are the values

    for item in range(memory.getSize()): # loop over all items
        value = memory.read(item) # read the item
        items[value] = items.get(value, 0) + 1 # if the key doesnt have a occurance value in dictionary, add it (0) and add 1
        if items[value] > 1: # if occurances are greater than 1, theres duplicates
            return True
    return False

def selectionSort(memory: Memory):
    """
    sorts the internal list in ascending order the custom class 'memory'

    Args:
        memory (Memory): the custom class that simulates computer memory
    
    Returns:
        list (list): the sorted list

    Raises:
        Nothing

    """
    # iterate through every index, finding the lowest value that should be in said index
    for index in range(memory.getSize() -1):

        lowestValue = memory.read(index)
        lowestIndex = index

        # find the lowest value in the rest of the array
        for index2 in range(index + 1, memory.getSize()):
            currentValue = memory.read(index2)
            # if a new lower value is found, store it and its index
            if currentValue < lowestValue:
                lowestValue = currentValue
                lowestIndex = index2
        
        # if a lower value was found, swap the positions
        if index != lowestIndex:
            memory.swap(index, lowestIndex)

    # The list is sorted after going through every index
    return memory.getList()


mem = Memory(10)
# mem.loadList([12, 54, 112, 5, 23, 89, 120, 58, 4, 1])
mem.loadList([12122, 5423, 1121, 523, 123, 89, 12, 5, 4, 1])

print(hasDuplicates(mem), mem.getOperations())
mem.resetOperations()

print(bubbleSort(mem), mem.getOperations())
mem.resetOperations()

print(selectionSort(mem), mem.getOperations())
mem.resetOperations()