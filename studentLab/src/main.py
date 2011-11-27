from domain.students import Student
from repository.repoSt import repoSt
from repository.repoA import repoA
from repository.memory import inMemory
from domain.validators import validateStudent, validateAssignment
from ui.ui import consoleUI

valSt = validateStudent()
valAsg = validateAssignment()

repositoryAssignmnent = repoA(valAsg)
repositoryStudent = repoSt(valSt)

inmemory = inMemory(repositoryStudent,repositoryAssignmnent)
inmemory.updateStudents()
inmemory.updateAssignments()

ui = consoleUI(repositoryStudent,repositoryAssignmnent)
ui.showMain()

#repository.storeSt(st2)
#while True:
#    try:
#        name = raw_input("name=")
#        id = raw_input("id=")
#        group = raw_input("group=")
#        st3 = Student(id , name , group)
#        repository.storeSt(st3)
#        break
#    except repoStException :
#        print "duplicate id"
#    except validatorException, e :
#        print e.getErrors()
#
#students = repository.getAll()    
#for asd in students :
#    print asd.getId()
    
