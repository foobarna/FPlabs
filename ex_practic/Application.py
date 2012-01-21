from repository.LabRepository import LabRepository
from repository.StudentRepository import StudentRepository
from ui.LabController import LabController
from ui.LabUI import LabUI

def run():
    stRepo = StudentRepository('repository/student.txt')
    labRepo = LabRepository("repository/lab.txt")
    labCtrl = LabController(stRepo, labRepo)
    labUI = LabUI(labCtrl)
    labUI.run()

run()
