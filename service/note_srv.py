from domain.entitati import note
from domain.validatori import NotaValidator
from repository.studenti_repo import OperatiiStudenti
from repository.probleme_repo import OperatiiProbleme
from repository.note_repo import OperatiiNote

class NoteService():
    def __init__(self, repo, validator):
        """
            Initializam clasa
        """
        self.__repo = repo
        self.__validator = validator

    def add_nota(self, id1, id2, nota_data):
        """
            Adaugam o nota unui student pe o problema
        """
        nota = note(id1, id2, nota_data)
        self.__validator.valideaza_nota(nota)
        self.__repo.adauga_nota(nota)
        return nota

    def delete_nota(self, id1, id2):
        """
            Stergem o nota
        """
        self.__repo.sterge_nota(id1, id2)

    def modify_nota(self, id1, id2, nota_noua):
        notaNoua = note(id1, id2, nota_noua)
        self.__validator.valideaza_nota(notaNoua)
        self.__repo.modifica_nota(id1, id2, nota_noua)
        return notaNoua

    def get_note(self):
        """
            Returnam toate notele
        """
        return self.__repo.returneaza_note()