from domain.assignments import Assignment
from domain.students import Student

class validatorException(Exception):
    def __init__(self, errors):
        self.errors = errors

    def getErrors(self):
        return self.errors
    
    def printErrors(self):
        for line in self.errors :
            print 13*" " + "WARNING!>>> " + line

class validateStudent:
    def __init__(self):
        pass
    
    def valid(self,st):
        errors = []
        if st.id == "" :
            errors.append("The field ID can not be  empty!")
        if st.name == "" :
            errors.append("The field NAME can not be empty!")
        if st.group == "" :
            errors.append("The field GROUP can not be empty!")
        if errors != [] :
            raise validatorException(errors)
        
class validateAssignment:
    def __init__(self):
        pass
    
    def valid(self,assi):
        errors=[]
        if assi.id == "" :
            errors.append("Field ID is empty")
        if assi.desc == "" :
            errors.append("Field Description is empty")
        if assi.deadline == "" :
            errors.append("Field Deadline is empty")
        if assi.grade == "" :
            errors.append("Field Grade is empty")
        if errors != [] :
            raise validatorException(errors)

def testvalidateStudent():
    st = Student("4", "", "913")
    validatorStudent = validateStudent()
    assert validatorStudent.valid(st).errors != []

def testCreateStudent():
    st = Student("4", "Ionescu", "913")
    assert st.getId() == "4"
    assert st.getName() == "Ionescu"
    assert st.getGroup() == "913"

def testStudentisValid():
    st = Student("5", "", "123")
    assert st.isValid()==False
    
    st = Student("", "Ionescu", "135")
    assert st.isValid()==False
    
    st = Student("52", "Ionescu", "134")
    assert st.isValid()==True

def testStudentisValid2():
    st = Student("", "", "914")
    errors = st.getErrors()
    assert len(errors)==2
    
    st = Student("", "Ionescu", "913")
    errors = st.getErrors()
    assert len(errors)==1
    
def testCreateAssignment():
    assi = Assignment("234" , "this blows" , "4" , "6")
    assert assi.getId() == "234"
    assert assi.getDeadline() == "4"
    assert assi.getDesc() == "this blows"
    assert assi.getGrade() == "6"
    
def testAssignmentisValid():
    assi = Assignment("234" , "" , "4" , "6")
    assert assi.isValid() == False
    
    assi = Assignment("234" , "this blows" , "4" , "")
    assert assi.isValid() == False
    
    assi = Assignment("" , "this blows" , "4" , "6")
    assert assi.isValid() == False
    
    assi = Assignment("234" , "this blows" , "" , "")
    assert len(assi.getErrors()) == 2
    
    assi = Assignment("" , "" , "4" , "")
    assert len(assi.getErrors()) == 3
    
testCreateStudent()
testStudentisValid()
testStudentisValid2()
testCreateAssignment()
testAssignmentisValid()
