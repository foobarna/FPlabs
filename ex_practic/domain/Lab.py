class Lab():
    def __init__(self, studentId, labNumber, problemNumber):
        self.studentId = int(studentId)
        self.labNumber = int(labNumber)
        self.problemNumber = str(problemNumber)

    def __str__(self):
        return str(str(self.studentId) + " " + str(self.labNumber) + " " + self.problemNumber)
