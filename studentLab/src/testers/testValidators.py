from domain.validators import validatorException, validateStudent, validateAssignment
from domain.assignments import Assignment
from domain.students import Student
import unittest


class TestValidators(unittest.TestCase):

    def testValidateStudent(self):
        errors = []
        st = Student("4", "", "913")
        validatorStudent = validateStudent()
        try:
            assert validatorStudent.valid(st).errors != []
        except validatorException, e :
            pass

    def testCreateStudent(self):
        st = Student("4", "Ionescu", "913")
        assert st.getId() == "4"
        assert st.getName() == "Ionescu"
        assert st.getGroup() == "913"

    def testStudentisValid(self):
        st = Student("5", "", "123")
        assert st.isValid() == False

        st = Student("", "Ionescu", "135")
        assert st.isValid() == False

        st = Student("52", "Ionescu", "134")
        assert st.isValid() == True

    def testStudentisValid2(self):
        st = Student("", "", "914")
        errors = st.getErrors()
        assert len(errors) == 2

        st = Student("", "Ionescu", "913")
        errors = st.getErrors()
        assert len(errors) == 1

    def testCreateAssignment(self):
        assi = Assignment("234" , "this blows" , "4" , "6")
        assert assi.getId() == "234"
        assert assi.getDeadline() == "4"
        assert assi.getDesc() == "this blows"
        assert assi.getGrade() == "6"

    def testAssignmentisValid(self):
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

def suite():
    print "Test for Validators runned succesfuly "
    suite = unittest.TestSuite()
    suite.addTest(TestValidators("testValidateStudent"))
    suite.addTest(TestValidators("testCreateStudent"))
    suite.addTest(TestValidators("testStudentisValid"))
    suite.addTest(TestValidators("testStudentisValid2"))
    suite.addTest(TestValidators("testCreateAssignment"))
    suite.addTest(TestValidators("testAssignmentisValid"))

    print ""
    return suite

runner = unittest.TextTestRunner()
runner.run(suite())
