from repository.repoSt import repoSt, repoException
from domain.students import Student
from domain.validators import validatorException

class fileRepoSt(repoSt):
    def __init__(self,validator,fileName):
        repoSt.__init__(self, validator)
        self.fileName = fileName
        self.__fromFile()
        
    def __fromFile(self):
        file = open(self.fileName)
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            data = line.split()
            st = Student(data[0],data[1],data[2])
            self.students[st.getId()] = st
        file.close()
        
    def storeSt(self,st):
        repoSt.storeSt(self, st)
        self.fileStoreSt(st)
        
    def fileStoreSt(self,st):
        file = open(self.fileName,"a")
        line = st.getId() + " " + st.getName() + " " + st.getGroup() + '\n'
        file.write(line)
        file.close()
        
    def fileDelId(self,id):
#        file = open(self.fileName,'w')
#        file.
#        poz = file.tell()
#        line = file.readline()
#        for i in range(0,len(line)):
#            file.write(i," ")
        pass
            
        
    
    def delId(self,id):
        repoSt.delId(self, id)
        self.fileDelId(id)