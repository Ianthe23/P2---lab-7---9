from domain.entitati import Probleme
import os

def cautaProblema(lista, id, n):
    if n < 0:
        raise ValueError("Id-ul nu a fost gasit!")
    if float(lista[n - 1].get_nrlab_nrpb()) == id:
        return lista[n - 1]
    return cautaProblema(lista, id, n - 1)

def adaugareValida(lista, nrlab_nrpb, n):
    if n < 0:
        return True
    if float(lista[n - 1].get_nrlab_nrpb()) == nrlab_nrpb:
        raise ValueError("Nr lab si nr pb exista deja!")
    return adaugareValida(lista, nrlab_nrpb, n - 1)

class OperatiiProbleme:
    def __init__(self):
        """
            Initializam repository-ul cu o lista vida
        """
        self.__probleme = []
    
    def adauga_problema(self, noua_problema):
        """
            Adaugam o noua problema
        """
        problema = Probleme(noua_problema.get_nrlab_nrpb(), noua_problema.get_descriere(), noua_problema.get_deadline())
        if len(self.__probleme) > 0:
            if adaugareValida(self.__probleme, problema.get_nrlab_nrpb(), len(self.__probleme)):
                self.__probleme.append(problema)
        else:
            self.__probleme.append(problema)

    def sterge_problema(self, nrlab_nrpb):
        """
            Stergem problemele dupa nr lab si nr pb
        """
        noi_probleme = []
        for problema in self.__probleme:
            if float(problema.get_nrlab_nrpb()) != nrlab_nrpb:
                noi_probleme.append(problema)
        self.__probleme = noi_probleme

    def modifica_problema(self, nrlab_nrpb, descriere_noua, deadline_nou):
        """
            Modificam problema identificata dupa nr lab si nr pb
        """
        noi_probleme = []
        for problema in self.__probleme:
            if float(problema.get_nrlab_nrpb()) == nrlab_nrpb:
                problema.set_descriere(descriere_noua)
                problema.set_deadline(deadline_nou)
            noi_probleme.append(problema)
        self.__probleme = noi_probleme

    def cauta_nrlab_nrpb(self, nrlab_nrpb):
        """
            Cautam sa vedem daca nr lab si nr pb apartine deja unei probleme
        """
        return cautaProblema(self.__probleme, nrlab_nrpb, len(self.__probleme))
        
    def returneaza_probleme(self):
        """
            Returnam lista de probleme
        """
        return self.__probleme
    
    def __eq__(self, other):
        if self.__probleme == other.__probleme:
            return True
        return False
    

class OperatiiProblemeFile(OperatiiProbleme):

    def __init__(self, filename):
        """
            Initializam repo-ul cu numele fisierului
        """
        OperatiiProbleme.__init__(self)
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
                nrlab_nrpb, descriere, deadline = [elem.strip() for elem in line.split(", ")]
                problema = Probleme(nrlab_nrpb, descriere, deadline)
                OperatiiProbleme.adauga_problema(self, problema)

    def __save_in_file(self):
        """
            Salvam datele in fisier
        """
        with open(self.__filename, "w") as f:
            toate_problemele = OperatiiProbleme.returneaza_probleme(self)
            for problema in toate_problemele:
                problema_citita = str(problema.get_nrlab_nrpb()) + ", " + str(problema.get_descriere()) + ", " + str(problema.get_deadline()) + "\n"
                f.write(problema_citita)

    def adauga_problema(self, problema_noua):
        """
            Adaugam o problema noua
        """
        OperatiiProbleme.adauga_problema(self, problema_noua)
        self.__save_in_file()

    def sterge_problema(self, id):
        """
            Stergem o problema dupa id
        """
        OperatiiProbleme.sterge_problema(self, id)
        self.__save_in_file()

    def modifica_problema(self, id, nume_nou, grup_nou):
        """
            Modificam o problema dupa id
        """
        OperatiiProbleme.modifica_problema(self, id, nume_nou, grup_nou)
        self.__save_in_file()

    def cauta_nrlab_nrpb(self, id):
        """
            Returnam o problema dupa id
        """
        return OperatiiProbleme.cauta_nrlab_nrpb(self, id)
    
    def returneaza_probleme(self):
        """
            Returnam toate problemele
        """
        return OperatiiProbleme.returneaza_probleme(self)
    
    def __eq__(self, other):
        """
            Suprascrie metoda eq
        """
        return OperatiiProbleme.__eq__(self, other)
    