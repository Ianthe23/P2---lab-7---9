from domain.entitati import studenti, probleme
from repository.studenti_repo import OperatiiStudenti
from repository.probleme_repo import OperatiiProbleme

class OperatiiNote():
    def __init__(self):
        """
            Initializam clasa in care adaugam notele
        """
        self.__note = []

    def adauga_nota(self, id1, id2, nota):
        """
            Functia adauga nota pentru studentul cu id-ul id1 si
            pentru laboratorul cu nr lab si nr pb id2
        """
        if not len(self.__note):
            self.__note.append([id1, id2, nota])
        else:
            for index in range(len(self.__note)):
                if self.__note[index][0] == id1 and self.__note[index][1] == id2:
                    raise ValueError("Nu i se poate asigna o alta nota pentru aceeasi problema!")
            self.__note.append([id1, id2, nota])


    def sterge_nota(self, id1, id2):
        """
            Stergem nota asignata unui student si unui laborator
        """
        index = 0
        ok = True
        for index in range(len(self.__note)):
            if self.__note[index][0] == id1 and self.__note[index][1] == id2:
                self.__note.pop(index)
                ok = False
                break
        if ok:
            raise ValueError("Nu a fost gasita nota!")
        
    def modifica_nota(self, id1, id2, nota_noua):
        """
            Modificam nota unui student cu alta nota
        """
        index = 0
        ok = True
        for index in range(len(self.__note)):
            if self.__note[index][0] == id1 and self.__note[index][1] == id2:
                self.__note[index][2] = nota_noua
                ok = False
                break
        if ok:
            raise ValueError("Nu a fost gasita nota!")
    
    def returneaza_note(self):
        """
            Returnam toate notele
        """
        return self.__note
    
    def __eq__(self, other):
        return self.__note == other.__note
