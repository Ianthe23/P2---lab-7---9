from domain.entitati import Studenti, Probleme, Note
from repository.studenti_repo import OperatiiStudenti
from repository.probleme_repo import OperatiiProbleme
import os

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
        nota_noua = Note(nota.get_id_student(), nota.get_id_problema(), nota.get_nota())

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
            if int(nota.get_id_student()) == id1 and float(nota.get_id_problema()) == id2:
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
            if int(nota.get_id_student()) == id1 and float(nota.get_id_problema()) == id2:
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
    
class OperatiiNoteFile(OperatiiNote):
    
    def __init__(self, filename):
        """
            Initializam repo-ul cu numele fisierului
        """
        OperatiiNote.__init__(self)
        file = os.path.abspath(filename)
        self.__filename = file
        self.__load_from_file()

    def __load_from_file(self):
        """
            Citim datele din fisier
        """
        with open(self.__filename, "r") as f:
            lines = f.readlines()
            for line in lines:
                if line == "\n":
                    break
                id_student, id_nrlab_nrpb, nota = [elem.strip() for elem in line.split(", ")]
                Nota = Note(id_student, id_nrlab_nrpb, nota)
                OperatiiNote.adauga_nota(self, Nota)

    def __save_in_file(self):
        """
            Salvam datele in fisier
        """
        with open(self.__filename, "w") as f:
            toate_notele = OperatiiNote.returneaza_note(self)
            for nota in toate_notele:
                nota_citita = str(nota.get_id_student()) + ", " + str(nota.get_id_problema()) + ", " + str(nota.get_nota()) + "\n"
                f.write(nota_citita)
        
    def adauga_nota(self, nota_noua):
        """
            Adaugam o nota noua
        """
        OperatiiNote.adauga_nota(self, nota_noua)
        self.__save_in_file()

    def sterge_nota(self, id1, id2):
        """
            Stergem o nota dupa id student si id problema
        """
        OperatiiNote.sterge_nota(self, id1, id2)
        self.__save_in_file()

    def modifica_nota(self, id1, id2, nota_noua):
        """
            Modificam o nota dupa id student si id problema
        """
        OperatiiNote.modifica_nota(self, id1, id2, nota_noua)
        self.__save_in_file()
    
    def returneaza_note(self):
        """
            Returnam toate notele
        """
        return OperatiiNote.returneaza_note(self)
    
    def __eq__(self, other):
        """
            Suprascrie metoda eq
        """
        return OperatiiNote.__eq__(self, other)
    


