import unittest

from domain.entitati import note, studenti
from domain.validatori import NotaValidator, StudentValidator
from repository.note_repo import OperatiiNote, OperatiiNoteFile
from repository.studenti_repo import OperatiiStudenti, OperatiiStudentiFile
from service.note_srv import NoteService
from service.studenti_srv import StudentService

class TestNoteService(unittest.TestCase):
    def setUp(self) -> None:
        self.__note_repo = OperatiiNote()
        self.__note_validator = NotaValidator()
        self.__studenti_srv = StudentService(OperatiiStudenti(), StudentValidator())
        self.__note_srv = NoteService(self.__note_repo, self.__note_validator, self.__studenti_srv)

    def test_add_nota(self):
        nota = self.__note_srv.add_nota(317, 1.1, 10)
        self.assertEqual(nota.get_id_student(), 317)
        self.assertEqual(nota.get_id_problema(), 1.1)
        self.assertEqual(nota.get_nota(), 10)

        self.assertRaises(ValueError, self.__note_srv.add_nota, 317, 1, 1)

    def test_delete_nota(self):
        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(317, 1.2, 8)

        self.__note_srv.delete_nota(317, 1.1)
        self.assertEqual(len(self.__note_srv.get_note()), 1)

        self.__note_srv.delete_nota(317, 1.2)
        self.assertEqual(len(self.__note_srv.get_note()), 0)

    def test_modify_nota(self):
        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(317, 1.2, 8)

        nota1 = self.__note_srv.modify_nota(317, 1.1, 9)
        self.assertEqual(nota1.get_id_student(), 317)
        self.assertEqual(nota1.get_id_problema(), 1.1)
        self.assertEqual(nota1.get_nota(), 9)
        self.assertRaises(ValueError, self.__note_srv.modify_nota, 319, 1, 2)
    
    def test_creeare_raport(self):
        student1 = self.__studenti_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__studenti_srv.add_student(318, "Achim Eduard", 2)

        self.assertEqual(len(self.__studenti_srv.get_studenti()), 2)

        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(318, 1.2, 9)

        self.assertEqual(self.__note_srv.creeare_raport(), [[317, "Alexe Andrei", 1.1, 10], [318, "Achim Eduard", 1.2, 9]])

    def test_raport_crescator_nume(self):
        student1 = self.__studenti_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__studenti_srv.add_student(318, "Achim Eduard", 2)

        self.assertEqual(len(self.__studenti_srv.get_studenti()), 2)

        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(318, 1.2, 9)

        self.assertEqual(self.__note_srv.raport_crescator_nume(), [[318, "Achim Eduard", 1.2, 9], [317, "Alexe Andrei", 1.1, 10]])

        nota3 = self.__note_srv.add_nota(317, 1.2, 8)

        self.assertEqual(self.__note_srv.raport_crescator_nume(), [[318, "Achim Eduard", 1.2, 9], [317, "Alexe Andrei", 1.1, 10], [317, "Alexe Andrei", 1.2, 8]])

    def test_raport_crescator_nota(self):
        student1 = self.__studenti_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__studenti_srv.add_student(318, "Achim Eduard", 2)

        self.assertEqual(len(self.__studenti_srv.get_studenti()), 2)

        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(318, 1.2, 9)

        self.assertEqual(self.__note_srv.raport_crescator_nota(), [[318, "Achim Eduard", 1.2, 9], [317, "Alexe Andrei", 1.1, 10]])

        nota3 = self.__note_srv.add_nota(317, 1.2, 8)

        self.assertEqual(self.__note_srv.raport_crescator_nota(), [[317, "Alexe Andrei", 1.2, 8], [318, "Achim Eduard", 1.2, 9], [317, "Alexe Andrei", 1.1, 10]])

    def test_raport_medie(self):
        student1 = self.__studenti_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__studenti_srv.add_student(318, "Achim Eduard", 2)

        self.assertEqual(len(self.__studenti_srv.get_studenti()), 2)

        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(318, 1.2, 9)

        self.assertEqual(self.__note_srv.raport_medie_mai_mica_decat_5(), [[317, "Alexe Andrei", 1.1, 10, 10], [318, "Achim Eduard", 1.2, 9, 9]])

        nota3 = self.__note_srv.add_nota(317, 1.2, 6)

        self.assertEqual(self.__note_srv.raport_medie_mai_mica_decat_5(), [[317, "Alexe Andrei", 1.1, 10, 8], [317, "Alexe Andrei", 1.2, 6, 8], [318, "Achim Eduard", 1.2, 9, 9]])

    def test_raport_primii_10_studenti(self):
        student1 = self.__studenti_srv.add_student(317, "Alexe Andrei", 1)
        student2 = self.__studenti_srv.add_student(318, "Achim Eduard", 2)

        self.assertEqual(len(self.__studenti_srv.get_studenti()), 2)

        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(318, 1.2, 9)
        nota3 = self.__note_srv.add_nota(317, 1.2, 9)

        self.assertEqual(self.__note_srv.raport_primii_10_studenti(), [[318, "Achim Eduard", 1.2, 9], [317, "Alexe Andrei", 1.2, 9], [317, "Alexe Andrei", 1.1, 10]])

        nota4 = self.__note_srv.add_nota(318, 1.1, 8)

        self.assertEqual(self.__note_srv.raport_primii_10_studenti(), [[318, "Achim Eduard", 1.1, 8], [318, "Achim Eduard", 1.2, 9], [317, "Alexe Andrei", 1.2, 9], [317, "Alexe Andrei", 1.1, 10]])


    def test_get_note(self):
        nota1 = self.__note_srv.add_nota(317, 1.1, 10)
        nota2 = self.__note_srv.add_nota(317, 1.2, 8)
        
        self.assertEqual(len(self.__note_srv.get_note()), 2)


if __name__ == '__main__':
    unittest.main()