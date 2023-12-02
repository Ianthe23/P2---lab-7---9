from domain.entitati import Probleme
from domain.validatori import ProblemaValidator
from repository.probleme_repo import OperatiiProbleme, OperatiiProblemeFile
from utils.functions import string_generator, data_generator
from datetime import datetime, timedelta
import random
from random import uniform

class ProblemaService:
    def __init__(self, repo, validator):
        self.__repo = repo
        self.__validator = validator

    def add_problema(self, nrlab_nrpb, descriere, deadline):
        """
            Inseram o problema noua in repo
        """
        problema = Probleme(nrlab_nrpb, descriere, deadline)
        self.__validator.valideaza_problema(problema)
        self.__repo.adauga_problema(problema)
        return problema
    
    def delete_problema(self, nrlab_nrpb):
        """
            Stergem problema cu nr de lab si nr de pb dat
        """
        self.__repo.sterge_problema(nrlab_nrpb)

    def modify_problema(self, nrlab_nrpb, descriere_noua, deadline_nou):
        """
            Modificam problema identificata dupa nrlab si nrpb
        """
        problema = Probleme(nrlab_nrpb, descriere_noua, deadline_nou)
        self.__validator.valideaza_problema(problema)
        self.__repo.modifica_problema(nrlab_nrpb, descriere_noua, deadline_nou)
        return problema
    
    def search_nrlab_nrpb(self, nrlab_nrpb):
        """
            Cautam problema dupa nrlab si nrpb introdus
        """
        problema = self.__repo.cauta_nrlab_nrpb(nrlab_nrpb)
        return problema
    
    def get_probleme(self):
        """
            Returnam lista de probleme
        """
        return self.__repo.returneaza_probleme()
    
    def add_random_probleme(self, nr):
        """
            Adaugam random probleme
        """
        for index in range(nr):
            problema = Probleme(uniform(1.0, 10.0), string_generator(11), data_generator())
            self.__validator.valideaza_problema(problema)
            self.__repo.adauga_problema(problema)
