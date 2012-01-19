from domain.students import Student

import unittest

class TestStudent(unittest.TestCase):

    def testStudent(self):
        st = Student(13, 'cici', 342)
        assert st.getName() == 'cici'
        assert st.getId() == 13
        assert st.getGroup() == 342

    def testIsValid(self):
        st = Student('15', 'marie', '123')
        assert st.isValid() == True

    def testGetErrors(self):
        st = Student('32', '', '')
        assert st.getErrors() != []

def suite():
    print "Test for Student ran successfully"
    suite = unittest.TestSuite()
    suite.addTest(TestStudent("testStudent"))
    suite.addTest(TestStudent("testIsValid"))
    suite.addTest(TestStudent("testGetErrors"))
    print '\n'
    return suite

runnerS = unittest.TextTestRunner()
runnerS.run(suite())
