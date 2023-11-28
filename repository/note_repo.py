from domain.entitati import studenti, probleme, note
from repository.studenti_repo import OperatiiStudenti
from repository.probleme_repo import OperatiiProbleme

def adaugareValida(lista, id1, id2, n):
    if n < 0:
        return True
    if lista[n - 1].get_id_student() == id1:
        if lista[n - 1].get_id_problema() == id2:
            raise ValueError("Id-ul exista deja!")
    return adaugareValida(lista, id1, id2, n - 1)

class OperatiiNote():
    def __init__(self):
        """
            Initializam clasa in care adaugam notele
        """
        self.__note = []

    def adauga_nota(self, nota):
        """
            Functia adauga nota pentru studentul cu id-ul id1 si
            pentru laboratorul cu nr lab si nr pb id2
        """
        nota_noua = note(nota.get_id_student(), nota.get_id_problema(), nota.get_nota())

        if not len(self.__note):
            self.__note.append(nota_noua)
        else:
            if adaugareValida(self.__note, nota_noua.get_id_student(), nota_noua.get_id_problema(), len(self.__note)):
                self.__note.append(nota_noua)

    def sterge_nota(self, id1, id2):
        """
            Stergem nota asignata unui student si unui laborator
        """
        noi_note = []
        for nota in self.__note:
            if nota.get_id_student() == id1 and nota.get_id_problema() == id2:
                pass
            else:
                noi_note.append(nota)
        self.__note = noi_note
        
    def modifica_nota(self, id1, id2, nota_noua):
        """
            Modificam nota unui student cu alta nota
        """
        noi_note = []
        for nota in self.__note:
            if nota.get_id_student() == id1 and nota.get_id_problema() == id2:
                nota.set_nota(nota_noua)
            noi_note.append(nota)
        self.__note = noi_note
    
    def returneaza_note(self):
        """
            Returnam toate notele
        """
        return self.__note
    
    def __eq__(self, other):
        return self.__note == other.__note
