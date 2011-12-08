from repository.repoSt import repoException
from repository.repoA import repoA
from domain.assignments import Assignment
from domain.validators import validatorException

class fileRepoA(repoA):
    def __init__(self,validator,studentRepo,fileName):
        repoA.__init__(self, validator)
        self.fileName = fileName
        self.studentRepo = studentRepo
        self.importFile()
        
    def importFile(self):
        file = open(self.fileName,'r')
        while True :
            line = file.readline()
            if not line : break
            if line.isspace() : continue
            data = line.split()
            asg = Assignment(data[0],data[1],data[2],data[3])
            try:
                repoA.storeA(self, asg, self.studentRepo)
            except repoException,validatorException:
                pass
        file.close()
        
    def storeA(self,asg):
        repoA.storeA(self, asg, self.studentRepo)
        self.fileStoreA(asg)
        
    def fileStoreA(self,asg):
        file = open(self.fileName,"a")
        line = asg.getId() + " " + asg.getDesc() + " " + asg.getDeadline() + " " + asg.getGrade()
        file.write('\n')
        file.write(line)
        file.close()
        
    def fileDelAsg(self,id):
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
    
    def delAsg(self,id):
        repoA.delAsg(self, id)
        self.fileDelAsg(id)
        
    def updateAsg(self,asg):
        repoA.updateAsg(self,asg)
        self.fileDelAsg(asg.getId())
        self.fileStoreA(asg)