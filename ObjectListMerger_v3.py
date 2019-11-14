from inputData import inputData
import numpy

def getInput(dataNumber,inData):
    ''' Converts received data to data type objects
        Returns list of objects '''
    outList = []
    if len(inData) < 1 :
        outList.append( inputData(0, '-', 0, 0) )
    else:
        for i in inData:
            outList.append( inputData(dataNumber, i[0], i[1], i[2]) )
    return outList

def selector(data1, data2):
    ''' Returns the object with higher precision
        Returns an object '''
    selected = None
    if (data1.prec >= data2.prec):
        selected = data1
    else:
        selected = data2
    return selected

def getOutput(in1, in2):
    ''' Finds pair objects and calls selector function to get the better one
        Returns list of objects '''
    in1.sort(key=lambda x: x.prec , reverse=True)
    in1.sort(key=lambda x: x.objNum , reverse=False)
    in2.sort(key=lambda x: x.prec , reverse=True)
    in2.sort(key=lambda x: x.objNum , reverse=False)
    lst = []
    objCnt = 1
    for i in in1:
        for j in in2:
            if (i.objNum == j.objNum) and (i.objNum == objCnt) :
                s = selector(i,j)
                if s not in lst:
                    lst.append(s)
                    objCnt += 1
    return lst

def multiSelect(inData):
    ''' Enables comparement for more than two input lists by calling getOutput function as much as needed
        Returns list of objects '''
    result = []
    cnt = 0
    for i in range(int(len(inData)/2)):
        result.append(getOutput(inData[i+cnt], inData[i+cnt+1]))
        cnt += 1
    inData = result
    if len(inData) > 1:
        return(multiSelect(inData))
    else:
        return(inData)


if __name__ == '__main__':
    # input11 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]
    # input12 = [['knife',1, 55], ['scissor', 2, 95], ['fork', 3, 99], ['spoon', 4, 99], ['keys', 5, 95] ]
    #
    # input21 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]
    # input22 = [['keys', 5, 95], ['spoon', 4, 99], ['fork', 3, 99], ['scissor', 2, 95], ['knife',1, 55] ]

    input11 = [['knife',1, 89]]
    input12 = [['knife',1, 35]]
    input21 = [['knife',1, 69]]
    input22 = [['knife',1, 80]]

    in11 = getInput(1,input11)
    in12 = getInput(2,input12)
    in21 = getInput(3,input21)
    in22 = getInput(4,input22)

    outList = multiSelect([in11, in12, in21, in22])[0]

    outStr = []
    for a in outList:
        outStr.append('(' + a.objName + ',' + str(a.objNum) + ',' + str(a.prec) + '%' + ')')
    print(outStr)
    print(outStr)
