class Student:
    def __init__(self, id, name, group):
        self.id = id
        self.name = name
        self.group = group
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getGroup(self):
        return self.group

    def setId(self,id):
        self.id = id
        
    def setName(self,name):
        self.name = name
        
    def setGroup(self,group):
        self.group =group
        
    def isValid(self):
        return self.id != "" and self.name != "" and self.group != ""
    
    def getErrors(self):
        errors = []
        if self.id == "" :
            errors.append("The field ID is empty!")
        if self.name == "" :
            errors.append("The field NAME is empty!")
        if self.group == "" :
            errors.append("The field GROUP is empty!")
        return errors
            
