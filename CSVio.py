#Michael Major HW8: Summary Statistics

def median(vlist):
    if len(vlist) > 0:
        medianList = sorted(vlist)
        if len(medianList)%2 == 0:
            return (medianList[len(medianList)//2-1] + medianList[len(medianList)//2])/2
        else:
            return medianList[len(medianList)//2]
        
def stdev(vlist):
    ave = sum(vlist)/len(vlist)
    stdList = []
    for i in range(len(vlist)):
        stdList += [(vlist[i] - ave)**2]
    return (sum(stdList)/len(stdList))**0.5

def openfile():
    fileFound = False
    fileName = str(input('Enter filename: '))
    while not fileFound:
        try:
            file = open(fileName,'r')
            fileFound = True
        except FileNotFoundError:
            fileName = str(input('File not found. Please re-enter: '))
    return file

def fieldindex(ifile):
    validField = False
    numAttempts = 1
    fieldString = ifile.readline().strip()
    originalList = fieldString.split(',')
    lowerList = fieldString.lower().replace(" ","").split(',')
    fieldName = str(input('Enter fieldname: '))
    while not validField and numAttempts < 3:
        try:
            myIndex = lowerList.index(fieldName.lower().replace(" ",""))
            validField = True
        except ValueError:
            fieldName = str(input(fieldName + " does not match any field. Please re-enter: "))
            numAttempts += 1
    if not validField:
        return -1,""
    else:
        return myIndex,originalList[myIndex]
        
dataFile = openfile()
field,name = fieldindex(dataFile)
if field != -1:
    listOfStrings = dataFile.readlines()
    lines = []
    dataList = []
    for i in range(len(listOfStrings)):
        lines += [listOfStrings[i].replace('\n','').split(',')]
    validField = True
    try:
        int(lines[0][field])
    except ValueError:
        print(name,"is not a numeric field!\nProgram terminated.")
        validField = False
    if validField:
        dataList = []
        for i in range(len(lines)):
            dataList += [int(lines[i][field])]
        summaryString = name + " Summary Data"
        dashString = ""
        for i in range(len(summaryString)):
            dashString += "-"
        print(summaryString+"\n"+dashString)
        print("\tNumber of Scores:",len(dataList))
        print("\tMean:",sum(dataList)/len(dataList))
        print("\tStandardDeviation:",stdev(dataList))
        print("\tMedian:",median(dataList))
        print("\tMin:",min(dataList))
        print("\tMax:",max(dataList))
else:
    print('3 unsuccessful field searches have been made.\nProgram terminated.') 



