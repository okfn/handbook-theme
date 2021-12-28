
def getFileProperties(filePath):
    fileObj = open(filePath)
    res = {}
    state = 0
    for line in fileObj:
        if state == 0:
            if line.strip() != '---':
                return res
            state = 1
        elif state == 1:
            values = line.strip().split(':')
            

        