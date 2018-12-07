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
    outList = []
    for i in range(len(in1)):
        outList.append(selector(in1[i],in2[i]))
    return outList


if __name__ == '__main__':
    input1 = [['knife',1, 99], ['scissor', 2, 65], ['spoon', 3, 33], ['spoon', 4, 80], ['keys', 5, 95]]
    input2 = [['knife',1, 55], ['scissor', 2, 95], ['fork', 3, 99], ['spoon', 4, 99], ['keys', 5, 95] ]
    in1 = getInput(1,input1)
    in2 = getInput(2,input2)

    outList = getOutput(in1, in2)

    outStr = []
    for a in outList:
        outStr.append('(' + a.objName + ',' + str(a.objNum) + ',' + str(a.prec) + '%' + ')')
    print(outStr)
