import unittest
from domain.entitati import studenti, probleme, note

class test_studenti(unittest.TestCase):

    def test_creeare_studenti(self):
        student = studenti(317, "Alexe Andrei", 1)
        self.assertEqual(student.get_studentID(), 317)
        self.assertEqual(student.get_nume(), "Alexe Andrei")
        self.assertEqual(student.get_grup(), 1)

        student.set_nume("Alexe Andrei")
        student.set_grup(1)

        self.assertEqual(student.get_nume(), "Alexe Andrei")
        self.assertEqual(student.get_grup(), 1)
    
    def test_egali_studenti(self):
        student1 = studenti(317, "Alexe Andrei", 1)
        student2 = studenti(317, "Alexe Andrei", 1)

        self.assertEqual(student1, student2)

        student3 = studenti(317, "Alexe Andreea", 1)

        self.assertNotEqual(student1, student3)

class test_probleme(unittest.TestCase):

    def test_creeare_probleme(self):
        problema = probleme(1.2, "Da un exemplu de functie injectiva", "12/12/2023")
        self.assertEqual(problema.get_nrlab_nrpb(), 1.2)
        self.assertEqual(problema.get_descriere(), "Da un exemplu de functie injectiva")
        self.assertEqual(problema.get_deadline(), "12/12/2023")

        problema.set_descriere("Da un exemplu de functie bijectiva")
        problema.set_deadline("13/12/2023")

        self.assertEqual(problema.get_descriere(), "Da un exemplu de functie bijectiva")
        self.assertEqual(problema.get_deadline(), "13/12/2023")

    def test_egale_probleme(self):
        problema1 = probleme(1.2, "Da un exemplu de functie injectiva", "12/12/2023")
        problema2 = probleme(1.2, "Da un exemplu de functie injectiva", "12/12/2023")

        self.assertEqual(problema1, problema2)

        problema3 = probleme(1.3, "Da un exemplu de functie injectiva", "12/12/2023")

        self.assertNotEqual(problema1, problema3)

class test_note(unittest.TestCase):

    def test_creeare_nota(self):
        nota = note(317, 1.1, 10)
        self.assertEqual(nota.get_id_student(), 317)
        self.assertEqual(nota.get_id_problema(), 1.1)
        self.assertEqual(nota.get_nota(), 10)

        nota.set_id_problema(1.2)
        nota.set_nota(5)

        self.assertEqual(nota.get_id_problema(), 1.2)
        self.assertEqual(nota.get_nota(), 5)
    
    def test_egale_note(self):
        nota = note(317, 1.1, 10)
        nota1 = note(317, 1.1, 10)

        self.assertEqual(nota, nota1)

        nota2 = note(317, 1.2, 10)

        self.assertNotEqual(nota, nota2)

if __name__ == '__main__':
    unittest.main()