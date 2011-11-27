from repository.repoSt import repoException
from domain.validators import validatorException
from utils import *
import sys

class consoleUI:
    def __init__(self,repositoryStudent,repositoryAssignment):
        self.repositoryStudent = repositoryStudent
        self.repositoryAssignment = repositoryAssignment
        self.s = 3*">" + " "
        
    def showMain(self):
        print ""
        print self.s + "1 >Manage students list"
        print self.s + "2 >Manage assignments list"
        print self.s + "3 >Search student by ID"
        print self.s + "4 >Get statistics.."
        print self.s + "5 >Exit/Terminates the run"
        print
        while True:
            while True :
                try:
                    cmd = input("selection << ")
                    if cmd < 1 or cmd > 5 :
                        raise Exception()
                    break
                except (NameError,Exception):
                    print 20*" " + "WARNING!>>> " + "Must be an integer number from 1 to 5"
            if cmd == 1 :
                self.showManageSt()
            elif cmd == 2 :
                self.showManageAsg()
            elif cmd == 3 :
                self.searchStudent()
            elif cmd == 4 :
                self.showStatistics()
            elif cmd == 5 :
                sys.exit()
    
    def showManageSt(self):
        print ""
        print self.s + "1 >Add new student"
        print self.s + "2 >Update valid student"
        print self.s + "3 >Remove a student"
        print self.s + "4 >Print students"
        print self.s + "5 >Exit/Terminates the run"
        print
        while True:
            while True :
                try:
                    cmd = input("selection << ")
                    if cmd < 1 or cmd > 5 :
                        raise Exception()
                    break
                except (NameError,Exception):
                    print 13*" " + "WARNING!>>> " + "Must be an integer number from 1 to 5"
            if cmd == 1 :
                self.addStudent()
            elif cmd == 2 :
                self.updateStudent()
            elif cmd == 3 :
                self.removeStudent()
            elif cmd == 4 :
                self.printStudents()
            elif cmd == 5 :
                break
            break
    
    def showManageAsg(self):
        print
        print self.s + "1 >Add new assignment"
        print self.s + "2 >Update valid assignment"
        print self.s + "3 >Remove an assignment"
        print self.s + "4 >Print assignments"
        print self.s + "5 <Back"
        print
        while True:
            while True :
                try:
                    cmd = input("selection << ")
                    if cmd < 1 or cmd > 5 :
                        raise Exception()
                    break
                except (NameError,Exception):
                    print 13*" " + "WARNING!>>> " + "Must be an integer number from 1 to 5"
            if cmd == 1 :
                self.addAssignment()
            elif cmd == 2 :
                self.updateAssignment()
            elif cmd == 3 :
                self.delAssignment()
            elif cmd == 4 :
                self.printAssignments()
            elif cmd == 5 :
                self.showMain()
    
    def showStatistics(self):
        print
        print self.s + "1 >Get students with grades below 5"
        print self.s + "2 >Get students sorted alphabetically"
        print self.s + "3 <Back"
        print
        while True:
            while True :
                try:
                    cmd = input("selection << ")
                    if cmd < 1 or cmd > 3 :
                        raise Exception()
                    break
                except (NameError,Exception):
                    print 13*" " + "WARNING!>>> " + "Must be an integer number from 1 to 3"
            if cmd == 1 :
                self.showUnder5()
            elif cmd == 2 :
                self.showSortName()
            elif cmd == 3 :
                self.showMain()       
    
    def addStudent(self):
        try:
            st = getStudentUI()
            self.repositoryStudent.storeSt(st)
            print 5*" " + "Student " + st.getName() + " was saved ..."
        except repoException :
            print 13*" " + "WARNING!>>> " +"Duplicate ID!"
        except validatorException, e :
            e.printErrors()
            
    def printStudents(self):
        students = self.repositoryStudent.getAll()
        print "\n Students from the list: "
        print "%3s %-10s %3s" % ("ID", "Name", "Group")
        for ex in students :
            print printStLine(ex)
            
    def removeStudent(self):
        try:
            id = raw_input("Give student id: ")
            st = self.repositoryStudent.delId(id)
            self.repositoryAssignment.delAsg(id)
            print 5* " " + "Student " + st.getName() + " with id " + st.getId() + " was deleted. FOREVAH!!!"
        except repoException :
            print 13*" " + "WARNING!>>> " + "Void ID!"
            
    def updateStudent(self):
        try:
            st = getStudentUI()
            self.repositoryStudent.updateSt(st)
            print 5*" " + "Updated!"
        except repoException :
            print 13*" " + "WARNING!>>>" +" ID dosent exist!"
        except validatorException, e:
            e.printErrors()
            
    def searchStudent(self):
        id = raw_input("Give student id: ")
        st = self.repositoryStudent.findId(id)
        if st == None :
            print 5*" " + "Student " + id + " was not found!"
        else :
            print 5*" " + "Student found! \n  " + printStLine(st)
     
    def addAssignment(self):
        try:
            asg = getAssignmentUI()
            self.repositoryAssignment.storeA(asg,self.repositoryStudent)
            st = self.repositoryStudent.findId(asg.getId())
            print 5*" " + "Assignment " + asg.getDesc() + " was saved for student " + st.getName() + " ..."
        except repoException :
            if self.repositoryAssignment.ok :
                print 13*" " + "WARNING!>>> " + "Cant save an assignment for a void student ID"
            if not self.repositoryAssignment.ok :
                print 5*" " + "Duplicate ID"
        except validatorException, e :
            e.printErrors()
            
    def delAssignment(self):
        try:
            asg = getAssignmentUI()
            self.repositoryAssignment.delAsg(asg.getId())
            print 5*" " + "Assignment for student " + asg.getId() + " deleted .... :-s"
        except repoException :
            print 13*" " + "WARNING!>>> " +"ID not found!"
        except validatorException, e :
            e.printErrors()
            
    def updateAssignmnent(self):
        try:
            asg = getAssignmentUI()
            self.repositoryAssignment.updateAsg(asg)
            print 5*" " + "Assignment updated!"
        except repoException :
            print 13*" " + "WARNING!>>> " +"ID not found"
        except validatorException, e :
            e.printErrors()
            
    def printAssignments(self):
        assignments = self.repositoryAssignment.getAll()
        for asg in assignments :
            print printAsgLine(asg)
            
    def showUnder5(self):
        assignments = self.repositoryAssignment.getAll()
        for asg in assignments :
            if asg.getGrade() < '5' :
                st = self.repositoryStudent.findId(asg.getId())
                print printStLine(st) + " with a grade of " + asg.getGrade()

    def showSortName(self):
        students = sortSt(self.repositoryStudent)
        for st in students :
            asg = self.repositoryAssignment.getById(st.getId())
            if asg != None :
                print st.getId() + " " + st.getName() + " with a grade of " + asg.getGrade()
            else :
                print st.getId() + " " + st.getName() + " with no grade "

