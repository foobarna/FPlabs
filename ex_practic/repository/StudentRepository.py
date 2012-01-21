from domain.Student import Student

class StudentRepository():
    def __init__(self, fileName):
        self.fileName = fileName
        self.students = {}
        self.loadFromFile()

    def loadFromFile(self):
        file = open(self.fileName, 'r')
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            data = line.split()
            id = int(data[0])
            name = ''
            for i in range(1, len(data)):
                if i != len(data) - 1 :
                    name += data[i] + " "
                else :
                    name += data[i]
            student = Student(id, name)
            self.students[id] = student
        return

    def findById(self, id):
        if id in self.students:
            st = self.students[id]
            return st
        else : return None

def test():
    a = StudentRepository('student.txt')
    for i in a.students.values():
        print i.name
    b = a.findById(5)
    print b.name

#test()
