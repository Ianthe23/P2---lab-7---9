from domain.entitati import probleme

def cautaProblema(lista, id, n):
    if n < 0:
        raise ValueError("Id-ul nu a fost gasit!")
    if lista[n - 1].get_nrlab_nrpb() == id:
        return lista[n - 1]
    return cautaProblema(lista, id, n - 1)

def adaugareValida(lista, nrlab_nrpb, n):
    if n < 0:
        return True
    if lista[n - 1].get_nrlab_nrpb() == nrlab_nrpb:
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
        problema = probleme(noua_problema.get_nrlab_nrpb(), noua_problema.get_descriere(), noua_problema.get_deadline())
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
            if problema.get_nrlab_nrpb() != nrlab_nrpb:
                noi_probleme.append(problema)
        self.__probleme = noi_probleme

    def modifica_problema(self, nrlab_nrpb, descriere_noua, deadline_nou):
        """
            Modificam problema identificata dupa nr lab si nr pb
        """
        noi_probleme = []
        for problema in self.__probleme:
            if problema.get_nrlab_nrpb() == nrlab_nrpb:
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