from domain.entitati import Note
from repository.note_repo import OperatiiNoteFile, OperatiiNote
import unittest

class TestOperatiiNote(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiNote()
        self.__repo1 = OperatiiNote()
        self.__repo2 = OperatiiNote()
        self.__repo3 = OperatiiNote()
        self.__new_repo = OperatiiNote()

    def test_eq(self):
        nota1 = Note(317, 1.1, 10)
        nota2 = Note(317, 1.2, 8)

        self.__repo1.adauga_nota(nota1)
        self.__repo2.adauga_nota(nota1)
        self.assertEqual(self.__repo1, self.__repo2)

        self.__repo3.adauga_nota(nota2)
        self.assertNotEqual(self.__repo1, self.__repo3)

    def test_adauga_nota(self):
        nota = Note(317, 1.3, 10)

        self.__repo.adauga_nota(nota)
        
        self.assertEqual(len(self.__repo.returneaza_note()), 1)

    def test_sterge_nota(self):
        nota = Note(317, 1.4, 10)
        self.__repo.adauga_nota(nota)
        self.assertEqual(len(self.__repo.returneaza_note()), 1)

        self.__repo.sterge_nota(317, 1.4)
        self.assertEqual(len(self.__repo.returneaza_note()), 0)

    def test_modifica_nota(self):
        nota = Note(317, 1.5, 10)

        self.__repo.adauga_nota(nota)
        self.assertEqual(len(self.__repo.returneaza_note()), 1)

        self.__repo.modifica_nota(317, 1.5, 9)

        nota1 = Note(317, 1.5, 9)
        self.__new_repo.adauga_nota(nota1)
        self.assertEqual(self.__repo, self.__new_repo)

    def test_returneaza_note(self):
        nota = Note(317, 1.6, 10)
        self.__repo.adauga_nota(nota)
        self.assertEqual(self.__repo.returneaza_note(), [nota])


class TestOperatiiNoteFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiNoteFile("test_note.txt")

    def test_create_file_Repo(self):
        init_len = len(self.__repo.returneaza_note())
        nota = Note(317, 2.1, 10)
        self.__repo.adauga_nota(nota)

        self.assertEqual(len(self.__repo.returneaza_note()), init_len + 1)

    def test_modify_fileRepo(self):
        init_len = len(self.__repo.returneaza_note())
        nota = Note(320, 2.2, 8)

        self.__repo.adauga_nota(nota)
        self.__repo.modifica_nota(320, 2.2, 5)


if __name__ == '__main__':
    unittest.main()
        