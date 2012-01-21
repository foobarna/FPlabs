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
            labId = studentId + labNumber           #we made this so that we have a unique key in our dictionary,    
                                                    #also it's the best way to raise exception if it there exists
                                                    #same studentId with the same labNumber.
            self.labs[labId] = lab
        return

    def findByStudentId(self, studentId):
        a = []
        for key in self.labs:
            if self.labs[key].studentId == studentId:
                a.append(self.labs[key])
        return a

    def add(self, lab):
        labId = str(lab.studentId) + str(lab.labNumber)
        self.labs[labId] = lab
        file = open(self.fileName, 'a')
        file.write('\n' + str(lab.studentId) + " " + str(lab.labNumber) + " " + str(lab.problemNumber))
        file.close()


def test():
    a = LabRepository('lab.txt')
    b = a.findByStudentId(5)
    for i in range(len(b)):
        print b[i].studentId, b[i].labNumber
    lab = Lab(100, 100, 100)
    a.add(lab)
    b = a.findByStudentId(100)
    for i in range(len(b)):
        print b[i].studentId, b[i].labNumber

#test()
