from domain.Lab import Lab

class LabRepository():
    def __init__(self, fileName):
        self.fileName = fileName
        self.labs = {}
        self.loadFromFile()

    def loadFromFile(self):
        file = open(self.fileName, 'r')
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            data = line.split()
            studentId = data[0]
            labNumber = data[1]
            problemNumber = data[2]
            lab = Lab(studentId, labNumber, problemNumber)
            self.labs[int(studentId)] = lab
        return
