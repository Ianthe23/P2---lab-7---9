from domain.entitati import note
from repository.note_repo import OperatiiNote
import unittest

class TestOperatiiNote(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiNote()
        self.__repo1 = OperatiiNote()
        self.__repo2 = OperatiiNote()
        self.__repo3 = OperatiiNote()
        self.__new_repo = OperatiiNote()

    def test_eq(self):
        self.__repo1.adauga_nota(317, 1.1, 10)
        self.__repo2.adauga_nota(317, 1.1, 10)
        self.assertEqual(self.__repo1, self.__repo2)

        self.__repo3.adauga_nota(317, 1.2, 8)
        self.assertNotEqual(self.__repo1, self.__repo3)

    def test_adauga_nota(self):
        self.__repo.adauga_nota(317, 1.1, 10)
        self.assertEqual(len(self.__repo.returneaza_note()), 1)

    def test_sterge_nota(self):
        self.__repo.adauga_nota(317, 1.1, 10)
        self.assertEqual(len(self.__repo.returneaza_note()), 1)

        self.__repo.sterge_nota(317, 1.1)
        self.assertEqual(len(self.__repo.returneaza_note()), 0)

    def test_modifica_nota(self):
        self.__repo.adauga_nota(317, 1.1, 10)
        self.assertEqual(len(self.__repo.returneaza_note()), 1)

        self.__repo.modifica_nota(317, 1.1, 9)

        self.__new_repo.adauga_nota(317, 1.1, 9)
        self.assertEqual(self.__repo, self.__new_repo)

    def test_returneaza_note(self):
        self.__repo.adauga_nota(317, 1.1, 10)
        self.assertEqual(self.__repo.returneaza_note(), [[317, 1.1, 10]])

if __name__ == '__main__':
    unittest.main()
        