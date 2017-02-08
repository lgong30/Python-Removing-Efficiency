import timeit
# from random_dense import setup, setup2
# from first_dense import setup, setup2
# from last_dense import setup, setup2
# from random_sparse import setup, setup2
# from first_sparse import setup, setup2
from last_sparse import setup, setup2

s1 = """\
if not isinstance(removalIndices, set):
    # print "Input is not a set, convert it"
    removalIndices = set(removalIndices)
[v for i, v in enumerate(myList) if not (i in removalIndices)]
"""

s2 = """\
for removalIndex in removalIndices[::-1]:
    try:
        del myList[removalIndex]
    except:
        print 'r = ', removalIndex, ', n = ', len(myList)
"""

s3 = """\
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
"""


t = [0] * 4
# print timeit.timeit(stmt=s1, setup=setup3, number=1) 

number = 5


for i in range(number):
    t[0] += timeit.timeit(stmt=s1, setup=setup2, number=1) 
    t[1] += timeit.timeit(stmt=s1, setup=setup, number=1) 
    t[2] += timeit.timeit(stmt=s2, setup=setup, number=1) 
    t[3] += timeit.timeit(stmt=s3, setup=setup, number=1) 

import numpy as np
print np.asarray(t) / number