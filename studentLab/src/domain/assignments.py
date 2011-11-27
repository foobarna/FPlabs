class Assignment:
    def __init__(self,id,desc,deadline,grade):
        self.id = id
        self.desc = desc
        self.deadline = deadline
        self.grade = grade
        
    def getId(self):
        return self.id

    def getDesc(self):
        return self.desc

    def getDeadline(self):
        return self.deadline

    def getGrade(self):
        return self.grade

    def setId(self,id):
        self.id = id

    def setDesc(self,desc):
        self.desc = desc

    def setDeadline(self,deadline):
        self.deadline = deadline

    def setGrade(self,grade):
        self.grade = grade
    
    def isValid(self):
        return self.id != "" and self.desc != "" and self.deadline != "" and self.grade != ""
    
    def getErrors(self):
        errors=[]
        if self.id == "" :
            errors.append("Field ID is empty")
        if self.desc == "" :
            errors.append("Field Description is empty")
        if self.deadline == "" :
            errors.append("Field Deadline is empty")
        if self.grade == "" :
            errors.append("Field Grade is empty")
        return errors
