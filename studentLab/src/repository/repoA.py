from repository.repoSt import repoException

class repoA:
    def __init__(self,validator):
        self.assignments = {}
        self.validateAsg = validator
        self.ok = False
        
    def storeA(self,asg,studentList):
        
        if asg.getId() not in studentList.students :
            self.ok = True
            raise repoException
            
        if asg.getId() in self.assignments :
            raise repoException    
            
        if (self.validateAsg != None) :
            self.validateAsg.valid(asg)
                    
        self.assignments[asg.getId()] = asg
        
    def delAsg(self,id):
        if id not in self.assignments :
            raise repoException
        
        del self.assignments[id]
        
    def updateAsg(self,asg):
        if asg.getId() not in self.assignments :
            raise repoException
            
        if (self.validateAsg != None) :
            self.validateAsg.valid(asg)
            
        updator = {}
        updator[asg.getId()] = asg
        
        self.assignments.update(updator)
    
    def getAll(self):
        return self.assignments.values()[:]

    def getById(self,id):
        if id in self.assignments :
            return self.assignments[id]
        else : return None
    
    def getLen(self):
        return len(self.assignments)
    