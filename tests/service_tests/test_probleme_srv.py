import unittest

from domain.entitati import Probleme
from domain.validatori import ProblemaValidator
from repository.probleme_repo import OperatiiProbleme
from service.probleme_srv import ProblemaService

class TestProblemaService(unittest.TestCase):
    def setUp(self) -> None:
        self.__test_repo = OperatiiProbleme()
        self.__test_valid = ProblemaValidator()
        self.__test_srv = ProblemaService(self.__test_repo, self.__test_valid)

    def test_add_problema(self):
        problema = self.__test_srv.add_problema(1.1, "Dati exemplu de functie injectiva", "01/01/2023")
        self.assertEqual(problema.get_nrlab_nrpb(), 1.1)
        self.assertEqual(problema.get_descriere(), "Dati exemplu de functie injectiva")
        self.assertEqual(problema.get_deadline(), "01/01/2023")

        self.assertRaises(ValueError, self.__test_srv.add_problema, 1.1, "", "01/01/2023")

    def test_delete_problema(self):
        problema1 = self.__test_srv.add_problema(1.1, "Dati exemplu de functie injectiva", "01/01/2023")
        problema2 = self.__test_srv.add_problema(1.2, "Dati exemplu de functie bijectiva", "02/01/2023")

        self.__test_srv.delete_problema(1.2)
        self.assertEqual(len(self.__test_srv.get_probleme()), 1)
    
    def test_modify_problema(self):
        problema1 = self.__test_srv.add_problema(1.1, "Dati exemplu de functie injectiva", "01/01/2023")
        problema2 = self.__test_srv.add_problema(1.2, "Dati exemplu de functie bijectiva", "02/01/2023")

        mod_problema = self.__test_srv.modify_problema(1.1, "Calculati raza", "03/01/2023")
        self.assertEqual(mod_problema.get_nrlab_nrpb(), 1.1)
        self.assertEqual(mod_problema.get_descriere(), "Calculati raza")
        self.assertEqual(mod_problema.get_deadline(), "03/01/2023")

        self.assertRaises(ValueError, self.__test_srv.modify_problema, 1.1, "", "03/01/2023")

    def test_search_nrlab_nrpb(self):
        problema1 = self.__test_srv.add_problema(1.1, "Dati exemplu de functie injectiva", "01/01/2023")
        problema2 = self.__test_srv.add_problema(1.2, "Dati exemplu de functie bijectiva", "02/01/2023")

        self.assertEqual(self.__test_srv.search_nrlab_nrpb(1.1), problema1)
        self.assertEqual(self.__test_srv.search_nrlab_nrpb(1.2), problema2)

        self.assertRaises(ValueError, self.__test_srv.search_nrlab_nrpb, 2)

    def test_get_probleme(self):
        problema1 = self.__test_srv.add_problema(1.1, "Dati exemplu de functie injectiva", "01/01/2023")
        problema2 = self.__test_srv.add_problema(1.2, "Dati exemplu de functie bijectiva", "02/01/2023")
    
        self.assertEqual(len(self.__test_srv.get_probleme()), 2)

if __name__ == '__main__':
    unittest.main()