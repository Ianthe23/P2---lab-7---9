import unittest

from domain.entitati import note
from domain.validatori import NotaValidator
from repository.note_repo import OperatiiNote
from service.note_srv import NoteService

class TestNoteService(unittest.TestCase):
    def setUp(self) -> None:
        self.__note_repo = OperatiiNote()
        self.__note_validator = NotaValidator()
        self.__note_srv= NoteService(self.__note_repo, self.__note_validator)

    def test_add_nota(self):
        nota = self.__note_srv.add_nota(317, 1.1, 10)
        self.assertEqual(nota.get_id_student(), 317)
        self.assertEqual(nota.get_id_problema(), 1.1)
        self.assertEqual(nota.get_nota(), 10)

        self.assertRaises(ValueError, self.__note_srv.add_nota, 317, 1, 1)

    def test_delete_nota(self):
        self.__note_srv.add_nota(317, 1.1, 10)
        self.__note_srv.add_nota(317, 1.2, 8)

        self.__note_srv.delete_nota(317, 1.1)
        self.assertEqual(len(self.__note_srv.get_note()), 1)

        self.__note_srv.delete_nota(317, 1.2)
        self.assertEqual(len(self.__note_srv.get_note()), 0)

    def test_modify_nota(self):
        self.__note_srv.add_nota(317, 1.1, 10)
        self.__note_srv.add_nota(317, 1.2, 8)

        self.__note_srv.modify_nota(317, 1.1, 9)
        lista = self.__note_srv.get_note()
        assert lista == [[317, 1.1, 9], [317, 1.2, 8]]

        self.__note_srv.modify_nota(317, 1.2, 10)
        lista = self.__note_srv.get_note()
        assert lista == [[317, 1.1, 9], [317, 1.2, 10]]


    def test_get_note(self):
        self.__note_srv.add_nota(317, 1.1, 10)
        self.__note_srv.add_nota(317, 1.2, 8)
        lista = self.__note_srv.get_note()
        assert lista == [[317, 1.1, 10], [317, 1.2, 8]]


if __name__ == '__main__':
    unittest.main()