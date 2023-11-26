import unittest

from domain.entitati import probleme
from repository.probleme_repo import OperatiiProbleme, cautaProblema, adaugareValida

class TestOperatiiProbleme(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiProbleme()
        self.__repo1 = OperatiiProbleme()
        self.__repo2 = OperatiiProbleme()
        self.__repo3 = OperatiiProbleme()
        self.__new_repo = OperatiiProbleme()

    def test_eq(self):
        problema1 = probleme(1.1, "Dati exemplu de functie bijectiva", "01/01/2023")
        problema2 = probleme(1.2, "Dati exemplu de functie injectiva", "02/01/2023")

        self.__repo1.adauga_problema(problema1)
        self.__repo2.adauga_problema(problema1)
        self.assertEqual(self.__repo1, self.__repo2)
        self.__repo3.adauga_problema(problema2)
        self.assertNotEqual(self.__repo1, self.__repo3)
        self.assertRaises(ValueError, self.__repo3.cauta_nrlab_nrpb, 1)

    def test_adauga_problema(self):
        problema = probleme(1.1, "Dati exemplu de functie bijectiva", "01/01/2023")

        self.__repo.adauga_problema(problema)
        self.assertEqual(len(self.__repo.returneaza_probleme()), 1)

    def test_sterge_problema(self):
        problema = probleme(1.1, "Dati exemplu de functie bijectiva", "01/01/2023")

        self.__repo.adauga_problema(problema)
        self.__repo.sterge_problema(1.1)
        self.assertEqual(len(self.__repo.returneaza_probleme()), 0)

    def test_modifica_problema(self):
        problema = probleme(1.1, "Dati exemplu de functie injectiva", "02/01/2023")

        self.__repo.adauga_problema(problema)
        self.__repo.modifica_problema(1.1, "Dati exemplu de functie injectiva", "01/01/2023")

        problema2 = probleme(1.1, "Dati exemplu de functie injectiva", "01/01/2023")

        self.__new_repo.adauga_problema(problema2)
        self.assertEqual(self.__repo, self.__new_repo)

    def test_cauta_nrlab_nrpb(self):
        problema1 = probleme(1.1, "Dati exemplu de functie injectiva", "01/01/2023")
        problema2 = probleme(1.2, "Dati exemplu de functie bijectiva", "02/01/2023")

        self.__repo.adauga_problema(problema1)
        self.__repo.adauga_problema(problema2)

        self.assertEqual(self.__repo.cauta_nrlab_nrpb(1.1), problema1)
        self.assertEqual(self.__repo.cauta_nrlab_nrpb(1.2), problema2)
        self.assertRaises(ValueError, self.__repo.cauta_nrlab_nrpb, 1)

    def test_returneaza_probleme(self):
        problema = probleme(1.1, "Dati exemplu de functie injectiva", "02/01/2023")
        
        self.__repo.adauga_problema(problema)
        self.assertEqual(self.__repo.returneaza_probleme(), [problema])

if __name__ == '__main__':
    unittest.main()