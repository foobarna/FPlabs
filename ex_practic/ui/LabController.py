from domain.Lab import Lab

class repoException(Exception):
    pass

class LabController:
    def __init__(self, StudentRepository, LabRepository):
        self.StRepo = StudentRepository
        self.LabRepo = LabRepository

    def addLab(self, studentId, labNumber, problemNumber):
        lab = Lab(studentId, labNumber, problemNumber)
        if lab in self.LabRepo.labs.values():
            raise repoException
        else :
            self.StRepo.add(lab)

    def getStudentById(self, studentId):
        return self.StRepo.findById(studentId)

    def getLabsByStudentId(self, studentId):
        return self.LabRepo.findByStudentId(studentId)
