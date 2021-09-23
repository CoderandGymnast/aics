import numpy as np

def split(list,numSegments,index):
    listSize=len(list)
    segmentSize=int(listSize/numSegments)
    
    firstSplitPoint=(index-1)*segmentSize
    if index==numSegments:
        return [list[firstSplitPoint:],list[:firstSplitPoint]]
    secondSplitPoint=index*segmentSize
    splittedSegment=list[firstSplitPoint:secondSplitPoint]
    remainingList=np.concatenate((list[:firstSplitPoint],list[secondSplitPoint:]))
    return [splittedSegment,remainingList]