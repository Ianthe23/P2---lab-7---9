import unittest

from domain.entitati import studenti
from domain.validatori import StudentValidator
from repository.studenti_repo import OperatiiStudenti
from service.studenti_srv import StudentService

class TestStudentService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_valid = StudentValidator()
        self.__test_repo = OperatiiStudenti()
        self.__test_srv = StudentService(self.__test_repo, self.__test_valid)

    def test_add_student(self):
        student = self.__test_srv.add_student(317, "Alexe Andrei", 1)
        self.assertEqual(student.get_studentID(), 317)
        self.assertEqual(student.get_nume(), "Alexe Andrei")
        self.assertEqual(student.get_grup(), 1)

        self.assertRaises(ValueError, self.__test_srv.add_student, 317, "", 1)

    def test_delete_student(self):
        student1 = self.__test_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__test_srv.add_student(318, "Alexe Maria", 2)

        self.__test_srv.delete_student(318)
        self.assertEqual(len(self.__test_srv.get_studenti()), 1)

        self.__test_srv.delete_student(317)
        self.assertEqual(len(self.__test_srv.get_studenti()), 0)

    def test_modify_student(self):
        student1 = self.__test_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__test_srv.add_student(318, "Alexe Maria", 2)

        student1 = self.__test_srv.modify_student(317, "Alexe Andreea", 1)
        self.assertEqual(student1.get_studentID(), 317)
        self.assertEqual(student1.get_nume(), "Alexe Andreea")
        self.assertEqual(student1.get_grup(), 1)
        self.assertRaises(ValueError, self.__test_srv.modify_student, 319, "", 2)

    def test_search_id(self):
        student1 = self.__test_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__test_srv.add_student(318, "Alexe Maria", 2)

        self.assertEqual(self.__test_srv.search_id(317), student1)
        self.assertEqual(self.__test_srv.search_id(318), student2)
        self.assertRaises(ValueError, self.__test_srv.search_id, 319)

    def test_get_studenti(self):
        student1 = self.__test_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__test_srv.add_student(318, "Alexe Maria", 2)

        self.assertEqual(len(self.__test_srv.get_studenti()), 2)

if __name__ == '__main__':
    unittest.main()