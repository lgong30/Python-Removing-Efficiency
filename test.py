import numpy as np 

def remove_with_move(myList, removalIndices):
    if not isinstance(removalIndices, set):
        # print "Input is not a set, convert it"
        removalIndices = set(removalIndices)
    return [v for i, v in enumerate(myList) if not (i in removalIndices)]

def remove(myList, removalIndices, inplace=False):
    if not inplace:
        return remove_with_move(myList, removalIndices)
    else:
        for removalIndex in removalIndices[::-1]:
            try:
                del myList[removalIndex]
            except:
                print 'r = ', removalIndex, ', n = ', len(myList)
        return myList

def efficient_remove(myList, removalIndices, inplace=False):
    if not inplace:
        return remove_with_move(myList, removalIndices)
    else:
        nextRemovalIndex = removalIndices[0]
        indexOfRemovalIndices = 1

        numOfRemovals = len(removalIndices)
        lenOfList = len(myList)

        currentIndex = nextRemovalIndex + 1
        while currentIndex < lenOfList:
            nextIndex = removalIndices[indexOfRemovalIndices] if indexOfRemovalIndices < numOfRemovals else lenOfList
            while currentIndex < nextIndex:
                myList[nextRemovalIndex] = myList[currentIndex]
                nextRemovalIndex += 1
                currentIndex += 1
            indexOfRemovalIndices += 1
            currentIndex += 1
        # pay attention
        myList[-numOfRemovals:] = []

        return myList

