from domain.students import Student
from domain.assignments import Assignment
from repository.repoSt import repoException
from domain.validators import validatorException

class inMemory:
    def __init__(self,repositoryStudent,repositoryAssignments):
        self.students = repositoryStudent
        self.asg = repositoryAssignments
    
    def presetStudents(self):
        list=[]
        st = Student("12" , "popa" , "413")
        list.append(st)
        st = Student("13" , "marie" , "513")
        list.append(st)
        st = Student("52" , "mihai" , "234")
        list.append(st)
        st = Student("17" , "arion" , "413")
        list.append(st)
        st = Student("56", "vasi" , "234")
        list.append(st)
        st = Student("22" , "ana" , "234")
        list.append(st)
        st = Student("7" , "ovidiu" , "413")
        list.append(st)
        st = Student("2", "pacala" , "513")
        list.append(st)
        st = Student("34" , "ofelia" , "413")
        list.append(st)
        st = Student("34" , "ofelia" , "413")
        list.append(st)
        st = Student("35" , "" , "413")
        list.append(st)
        return list
    
    def updateStudents(self):
        list = self.presetStudents()
        ok = False
        for st in list :
            try:
                self.students.storeSt(st)
            except repoException :
                print 13*" " + "WARNING!>>> " +"Duplicate ID!"
                ok = True                    
            except validatorException, e :
                e.printErrors()
                ok = True
        if ok == True :
            print 13*" " + "Errors while loading from memory!"
            
    def presetAssignments(self):
        list=[]
        asg1 = Assignment("12", "lab", "5", "6")
        list.append(asg1)
        asg1 = Assignment("13", "home", "7", "4")
        list.append(asg1)
        asg1 = Assignment("52", "lab", "6", "6")
        list.append(asg1)
        asg1 = Assignment("17", "lab", "4", "3")
        list.append(asg1)
        asg1 = Assignment("56", "home", "7", "4")
        list.append(asg1)
        asg1 = Assignment("7", "ex", "6", "7")
        list.append(asg1)
        asg1 = Assignment("2", "lab", "4", "6")
        list.append(asg1)
        return list
    
    def updateAssignments(self):
        list = self.presetAssignments()
        for asg in list :
            ok = False
            try:
                self.asg.storeA(asg,self.students)
            except repoException :
                ok = True
                if self.repositoryAssignment.ok :
                    print 13*" " + "WARNING!>>> " + "Cant save an assignment for a void student ID"
                elif not self.repositoryAssignment.ok :
                    print 5*" " + "Duplicate ID"
            except validatorException, e :
                ok = True
                e.printErrors()