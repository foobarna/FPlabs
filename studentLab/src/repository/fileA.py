from repository.repoSt import repoException
from repository.repoA import repoA
from domain.assignments import Assignment
from domain.validators import validatorException

class fileRepoSt(repoA):
    def __init__(self,validator,fileName):
        repoA.__init__(self, validator)
        self.fileName = fileName
        self.importFile()
        
    def importFile(self):
        file = open(self.fileName)
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            data = line.split()
            asg = Assignment(data[0],data[1],data[2],data[3])
            try:
                repoA.storeA(self, asg)
            except repoException,validatorException:
                pass
        file.close()
        
    def storeA(self,asg):
        repoA.storeA(self, asg)
        self.fileStoreA(asg)
        
    def fileStoreA(self,asg):
        file = open(self.fileName,"a")
        line = asg.getId() + " " + asg.getDesc() + " " + asg.getDeadline() + " " + asg.getGrade()
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
        repoA.delId(self, id)
        self.fileDelId(id)
        
    def updateSt(self,asg):
        repoSt.updateSt(self,st)
        self.fileDelId(asg.getId())
        self.fileStoreA(asg)