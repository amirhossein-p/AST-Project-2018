class inputData:
    def __init__(self,dataNum,objName,objNum,prec):
        self.dataNum = dataNum
        self.objName = objName
        self.objNum = objNum
        self.prec = prec

def getInput(dataNumber,inData):
    outList = []
    if len(inData) < 1 :
        outList.append( inputData(0, '-', 0, 0) )
    else:
        for i in inData:
            outList.append( inputData(dataNumber, i[0], i[1], i[2]) )
    return outList

def selector(data1, data2):
    selected = None
    if (data1.prec >= data2.prec):
        selected = data1
    else:
        selected = data2
    return selected

def getOutput(in1, in2):
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



if __name__ == '__main__':
    # input1 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]           # ok
    # input2 = [['knife',1, 55], ['scissor', 2, 95], ['fork', 3, 99], ['spoon', 4, 99], ['keys', 5, 95] ]

    # input1 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]           # ok
    # input2 = [['keys', 5, 95], ['spoon', 4, 99], ['fork', 3, 99], ['scissor', 2, 95], ['knife',1, 55] ]

    # input1 = []                                                                                                   # ok
    # input2 = []

    # input1 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33]]                                              # solved
    # input2 = []

    # input1 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33]]                                              # ok
    # input2 = [['KNIFE',1, 99], ['SCISSOR', 2, 65], ['SPOON', 3, 33]]

    # input1 = [['knife',1, 99], ['scissor', 2, 65]]                                                                # solved
    # input2 = [['fork', 3, 99], ['spoon', 4, 99]]

    input1 = [['knife',1, 99], ['knife',1, 69], ['knife',1, 89]]                                                    # solved
    input2 = [['knife',1, 99], ['fork', 3, 99]]

    in1 = getInput(1,input1)
    in2 = getInput(2,input2)

    outList = getOutput(in1, in2)

    outStr = []
    for a in outList:
        outStr.append('(' + a.objName + ',' + str(a.objNum) + ',' + str(a.prec) + '%' + ')')
    print(outStr)
