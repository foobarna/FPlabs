from domain.students import Student
from repository.repoSt import repoSt
from repository.repoA import repoA
from repository.memory import inMemory
from repository.fileSt import fileRepoSt
from domain.validators import validateStudent, validateAssignment
from ui.ui import consoleUI

valSt = validateStudent()
valAsg = validateAssignment()

repositoryAssignmnent = repoA(valAsg)
repositoryStudent = repoSt(valSt)
#repositoryStudent = fileRepoSt(valSt,"repository/studentsList")

inmemory = inMemory(repositoryStudent,repositoryAssignmnent)
inmemory.updateStudents()
inmemory.updateAssignments()

ui = consoleUI(repositoryStudent,repositoryAssignmnent)
ui.showMain()
