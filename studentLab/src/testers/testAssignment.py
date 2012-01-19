from domain.assignments import Assignment

import unittest

class TestAssignment(unittest.TestCase):

    def testAssignment(self):
        asg = Assignment('2', 'lab', '6', 5)
        assert asg.getDesc() == 'lab'
        assert not(asg.getId() == '52')

    def testIsValid(self):
        asg = Assignment('', '' , '4', 5)
        assert asg.isValid() == False
        assert asg.getDeadline() != ''

    def testGetErrors(self):
        asg = Assignment('', '', '', 5)
        assert asg.getErrors() != []
        assert len(asg.getErrors()) == 3
        asg = Assignment('5', 'do it', '6', 7)
        assert not(asg.getErrors() != [])

def suite():
    print "Test for Student ran successfully"
    suite = unittest.TestSuite()
    suite.addTest(TestAssignment("testAssignment"))
    suite.addTest(TestAssignment("testIsValid"))
    suite.addTest(TestAssignment("testGetErrors"))
    print '\n'
    return suite

runner = unittest.TextTestRunner()
runner.run(suite())

