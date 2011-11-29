class repoException(Exception):
    pass

class repoSt:
    def __init__(self,validator):
        self.students = {}
        self.validateSt = validator
        
    def storeSt(self,st):
        if st.getId() in self.students :
            raise repoException
            
        if (self.validateSt != None) :
            self.validateSt.valid(st)
                    
        self.students[st.getId()] = st
        
    def delId(self,id):
        if id not in self.students : 
            raise repoException
        st = self.students[id]
        del self.students[id]
        return st
    
    def getAll(self):
        return self.students.values()[:]
    
    def printSt(self):
        print self.students
        
    def getLen(self):
        return len(self.students)
    
    def updateSt(self,st):
        if st.getId() not in self.students :
            raise repoException
            
        if (self.validateSt != None) :
            self.validateSt.valid(st)
        
        updator = {}
        updator[st.getId()] = st
        
        self.students.update(updator)
        
    def findId(self,id):
        if id not in self.students :
            return None
        else :
            return self.students[id]