from domain.students import Student
from domain.assignments import Assignment

def getStudentUI():
    id = raw_input("Give student id: ")
    name = raw_input("Give student name: ")
    group = raw_input("Give student group: ")
    return Student(id, name, group)

def getAssignmentUI():
    id = raw_input("Give student id: ")
    desc = raw_input("Give assignmnet`s desc: ")
    deadline = raw_input("Give deadline: ")
    grade = raw_input("Give grade: ")
    return Assignment(id,desc,deadline,grade)

def printStLine(st):
    return "%3s %-10s %3s" % (st.getId(), st.getName(), st.getGroup())
    
def printAsgLine(asg):
    return "%3s %-10s %3s %2s" % (asg.getId(), asg.getDesc(), asg.getDeadline(), asg.getGrade())

def sortSt(repositorySt) :
    students = repositorySt.getAll()
    print len(students)
    for i in range(0,len(students)-1) :
        for j in range(i+1,len(students)) :
            if students[i].getName() > students[j].getName() :
                students[i], students[j] = students[j], students[i]
    return students
