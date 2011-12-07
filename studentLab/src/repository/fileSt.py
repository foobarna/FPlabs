from repository.repoSt import repoSt, repoException
from domain.students import Student
from domain.validators import validatorException

class fileRepoSt(repoSt):
    def __init__(self,validator,fileName):
        repoSt.__init__(self, validator)
        self.fileName = fileName
        self.importFile()
        
    def importFile(self):
        file = open(self.fileName)
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            data = line.split()
            st = Student(data[0],data[1],data[2])
            try:
                repoSt.storeSt(self, st)
            except repoException,validatorException:
                pass
        file.close()
        
    def storeSt(self,st):
        repoSt.storeSt(self, st)
        self.fileStoreSt(st)
        
    def fileStoreSt(self,st):
        file = open(self.fileName,"a")
        line = st.getId() + " " + st.getName() + " " + st.getGroup()
        file.write('\n')
        file.write(line)
        file.close()
        
    def fileDelId(self,id):
        file = open(self.fileName,'r')
        content = []
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            str = line.split()
            if id != str[0] :
                content.append(line)
        file.close()
        file = open(self.fileName,'w')
        file.writelines(content)
        file.close()
    
    def delId(self,id):
        repoSt.delId(self, id)
        self.fileDelId(id)
        
    def updateSt(self,st):
        repoSt.updateSt(self,st)
        self.fileDelId(st.getId())
        self.fileStoreSt(st)