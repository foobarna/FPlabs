from ui.LabController import repoException
from repository.LabRepository import LabRepository
from repository.StudentRepository import StudentRepository

class LabUI:
    def __init__(self, LabController):
        self.labCtrl = LabController

    def print_menu(self):
        print "1. Show activity for a given student ID"
        print "2. Add a lab for a given student ID"
        print "3. Exit"

    def run(self):
        while True:
            self.print_menu()
            o = int(raw_input("Type your option: "))
            if o == 1:
                studentId = input("    Give student ID: ")
                self.showStudentLabs(studentId)
            elif o == 2:
                studentId = input("    Give student ID: ")
                self.addStudentLab(studentId)
            elif o == 3:
                exit()


    def showStudentLabs(self, studentId):
        a = self.labCtrl.getLabsByStudentId(studentId)
        for i in range(len(a) - 1):
            for j in range(i + 1, len(a)):
                if a[i].labNumber > a[j].labNumber : a[i].labNumber, a[j].labNumber = a[j].labNumber, a[i].labNumber
        for i in range(len(a)):
            print a[i]

    def addStudentLab(self, studentId):
        st = self.labCtrl.getStudentById(studentId)
        labNumber = input('Give the number of the lab: ')
        problemNumber = input('Give the problem number: ')
        try:
            self.labCtrl.addLab(studentId, labNumber, problemNumber)
        except repoException():
            print "Same laboratory exists for the same student"


