from domain.entitati import studenti
from repository.studenti_repo import OperatiiStudenti, OperatiiStudentiFile, cautaStudent, adaugareValida
import unittest

class TestOperatiiStudenti(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiStudenti()
        self.__repo1 = OperatiiStudenti()
        self.__repo2 = OperatiiStudenti()
        self.__repo3 = OperatiiStudenti()
        self.__new_repo = OperatiiStudenti()
    
    def test_eq(self):
        student = studenti(317, "Alexe Andrei", 1)
        student1 = studenti(317, "Alexe Andreea", 1)

        self.__repo1.adauga_student(student)
        self.__repo2.adauga_student(student)
        self.assertEqual(self.__repo1, self.__repo2)

        self.__repo3.adauga_student(student1)
        self.assertNotEqual(self.__repo1, self.__repo3)
        self.assertRaises(ValueError, self.__repo1.cauta_ID, 5)

    def test_adauga_student(self):
        student = studenti(319, "Alexe Andrei", 1)

        self.__repo.adauga_student(student)

        self.assertEqual(len(self.__repo.returneaza_studenti()), 1)

    def test_sterge_student(self):
        student = studenti(320, "Alexe Andrei", 1)

        self.__repo.adauga_student(student)
        self.__repo.sterge_student(320)

        self.assertEqual(len(self.__repo.returneaza_studenti()), 0)

    def test_modifica_student(self):
        student = studenti(321, "Alexe Andrei", 1)

        self.__repo.adauga_student(student)
        self.__repo.modifica_student(321, "Alexe Andreea", 1)

        student1 = studenti(321, "Alexe Andreea", 1)
        self.__new_repo.adauga_student(student1)

        self.assertEqual(self.__repo, self.__new_repo)

    def test_cauta_ID(self):
        student = studenti(322, "Alexe Andrei", 1)
        self.__repo.adauga_student(student)

        student = studenti(323, "Alexe Maria", 2)
        self.__repo.adauga_student(student)
        self.assertEqual(self.__repo.cauta_ID(323), student)
        self.assertEqual(self.__repo.cauta_ID(322).get_nume(), "Alexe Andrei")
        self.assertRaises(ValueError, self.__repo.cauta_ID, 319)

    def test_returneaza_studenti(self):
        student = studenti(324, "Alexe Andrei", 1)

        self.__repo.adauga_student(student)

        self.assertEqual(self.__repo.returneaza_studenti(), [student])

class TestOperatiiStudentiFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiStudentiFile("test_studenti.txt")

    def test_create_file_Repo(self):
        init_len = len(self.__repo.returneaza_studenti())
        student = studenti(325, "Alexe Andrei", 1)
        self.__repo.adauga_student(student)

        self.assertEqual(len(self.__repo.returneaza_studenti()), init_len + 1)

    def test_modify_fileRepo(self):
        init_len = len(self.__repo.returneaza_studenti())
        student = studenti(326, "Alexe Andrei", 1)

        self.__repo.adauga_student(student)
        self.__repo.modifica_student(326, "Alexe Maria", 2)


if __name__ == '__main__':
    unittest.main()