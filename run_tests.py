import unittest
from tests.domain_tests.test_entitati import test_probleme, test_studenti, test_note
from tests.domain_tests.test_validatori import SValidator, PValidator, NValidator
from tests.repo_tests.test_probleme_repo import TestOperatiiProbleme
from tests.repo_tests.test_studenti_repo import TestOperatiiStudenti
from tests.repo_tests.test_note_repo import TestOperatiiNote
from tests.service_tests.test_probleme_srv import TestProblemaService
from tests.service_tests.test_studenti_srv import TestStudentService
from tests.service_tests.test_note_srv import TestNoteService


def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=test_probleme))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=test_studenti))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=test_note))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=SValidator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=PValidator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=NValidator))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestOperatiiProbleme))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestOperatiiStudenti))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestOperatiiNote))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestProblemaService))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestStudentService))
    test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(testCaseClass=TestNoteService))
    return test_suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
