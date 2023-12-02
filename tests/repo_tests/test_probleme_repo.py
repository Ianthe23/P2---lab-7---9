import unittest

from domain.entitati import Probleme
from repository.probleme_repo import OperatiiProbleme, OperatiiProblemeFile, cautaProblema, adaugareValida

class TestOperatiiProbleme(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiProbleme()
        self.__repo1 = OperatiiProbleme()
        self.__repo2 = OperatiiProbleme()
        self.__repo3 = OperatiiProbleme()
        self.__new_repo = OperatiiProbleme()

    def test_eq(self):
        problema1 = Probleme(1.1, "Dati exemplu de functie bijectiva", "01/01/2023")
        problema2 = Probleme(1.2, "Dati exemplu de functie injectiva", "02/01/2023")

        self.__repo1.adauga_problema(problema1)
        self.__repo2.adauga_problema(problema1)
        self.assertEqual(self.__repo1, self.__repo2)

        self.__repo3.adauga_problema(problema2)
        self.assertNotEqual(self.__repo1, self.__repo3)

        self.assertRaises(ValueError, self.__repo3.cauta_nrlab_nrpb, 1)

    def test_adauga_problema(self):
        problema = Probleme(1.3, "Dati exemplu de functie bijectiva", "01/01/2023")

        self.__repo.adauga_problema(problema)
        self.assertEqual(len(self.__repo.returneaza_probleme()), 1)

    def test_sterge_problema(self):
        problema = Probleme(1.4, "Dati exemplu de functie bijectiva", "01/01/2023")

        self.__repo.adauga_problema(problema)
        self.__repo.sterge_problema(1.4)
        self.assertEqual(len(self.__repo.returneaza_probleme()), 0)

    def test_modifica_problema(self):
        problema = Probleme(1.5, "Dati exemplu de functie injectiva", "02/01/2023")

        self.__repo.adauga_problema(problema)
        self.__repo.modifica_problema(1.5, "Dati exemplu de functie injectiva", "01/01/2023")

        problema2 = Probleme(1.5, "Dati exemplu de functie injectiva", "01/01/2023")

        self.__new_repo.adauga_problema(problema2)
        self.assertEqual(self.__repo, self.__new_repo)

    def test_cauta_nrlab_nrpb(self):
        problema1 = Probleme(1.6, "Dati exemplu de functie injectiva", "01/01/2023")
        problema2 = Probleme(1.7, "Dati exemplu de functie bijectiva", "02/01/2023")

        self.__repo.adauga_problema(problema1)
        self.__repo.adauga_problema(problema2)

        self.assertEqual(self.__repo.cauta_nrlab_nrpb(1.6), problema1)
        self.assertEqual(self.__repo.cauta_nrlab_nrpb(1.7), problema2)
        self.assertRaises(ValueError, self.__repo.cauta_nrlab_nrpb, 1)

    def test_returneaza_probleme(self):
        problema = Probleme(1.8, "Dati exemplu de functie injectiva", "02/01/2023")
        
        self.__repo.adauga_problema(problema)
        self.assertEqual(self.__repo.returneaza_probleme(), [problema])

class TestOperatiiProblemeFile(unittest.TestCase):
    def setUp(self) -> None:
        self.__repo = OperatiiProblemeFile("test_probleme.txt")

    def test_create_file_Repo(self):
        init_len = len(self.__repo.returneaza_probleme())
        problema = Probleme(2.1, "verif inj", "01/01/2023")
        self.__repo.adauga_problema(problema)

        self.assertEqual(len(self.__repo.returneaza_probleme()), init_len + 1)

    def test_modify_fileRepo(self):
        init_len = len(self.__repo.returneaza_probleme())
        problema = Probleme(2.2, "verif bij", "01/01/2023")

        self.__repo.adauga_problema(problema)
        self.__repo.modifica_problema(2.2, "verif surj", "02/01/2023")

if __name__ == '__main__':
    unittest.main()