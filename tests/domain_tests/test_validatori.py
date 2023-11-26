import unittest
from domain.entitati import studenti, probleme, note
from domain.validatori import StudentValidator, ProblemaValidator, NotaValidator

class SValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.__valid = StudentValidator()

    def test_valideaza_studentul(self):
        student = studenti(213, "Alexe Andrei", 1)
        self.__valid.valideaza_studentul(student)
        student = studenti(-213, "Alexe Andrei", 1)
        try:
            self.__valid.valideaza_studentul(student)
            assert False
        except ValueError:
            assert True
        student = studenti(213, "", 1)
        try:
            self.__valid.valideaza_studentul(student)
            assert False
        except ValueError:
            assert True
        student = studenti(213, "Alexe Andrei", -1)
        try:
            self.__valid.valideaza_studentul(student)
            assert False
        except ValueError:
            assert True

class PValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.__valid = ProblemaValidator()

    def test_valideaza_problema(self):
        problema = probleme(1.2, "Da un exemplu de functie injectiva", "12/12/2023")
        self.__valid.valideaza_problema(problema)
        problema = probleme(1, "Da un exemplu de functie injectiva", "12/12/2023")
        try:
            self.__valid.valideaza_problema(problema)
            assert False
        except ValueError:
            assert True
        problema = probleme(1.2, "", "12/12/2023")
        try:
            self.__valid.valideaza_problema(problema)
            assert False
        except ValueError:
            assert True
        problema = probleme(1.2, "Da un exemplu de functie injectiva", "31/04/2000")
        try:
            self.__valid.valideaza_problema(problema)
            assert False
        except ValueError:
            assert True

class NValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.__valid = NotaValidator()

    def test_valideaza_problema(self):
        nota = note(317, 1.1, 10)
        self.__valid.valideaza_nota(nota)
        nota = note(-10, 1.1, 10)
        try:
            self.__valid.valideaza_nota(nota)
            assert False
        except ValueError:
            assert True
        nota = note(317, 1, 10)
        try:
            self.__valid.valideaza_nota(nota)
            assert False
        except ValueError:
            assert True
        nota = note(317, 1.1, -10)
        try:
            self.__valid.valideaza_nota(nota)
            assert False
        except ValueError:
            assert True


if __name__ == '__main__':
    unittest.main()