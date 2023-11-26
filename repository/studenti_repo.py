from domain.entitati import studenti

def cautaStudent(lista, id, n):
    if n < 0:
        raise ValueError("Id-ul nu a fost gasit!")
    if lista[n - 1].get_studentID() == id:
        return lista[n - 1]
    return cautaStudent(lista, id, n - 1)

def adaugareValida(lista, id, n):
    if n < 0:
        return True
    if lista[n - 1].get_studentID() == id:
        raise ValueError("Id-ul exista deja!")
    return adaugareValida(lista, id, n - 1)

class OperatiiStudenti:
    def __init__(self):
        """
            Initializam repository-ul cu o lista vida
        """
        self.__studenti = []

    def adauga_student(self, nou_student):
        """
            Adaugam un nou student
        """
        student = studenti(nou_student.get_studentID(), nou_student.get_nume(), nou_student.get_grup())
        if len(self.__studenti) > 0:
            if adaugareValida(self.__studenti, student.get_studentID(), len(self.__studenti)):
                self.__studenti.append(student)
        else:
            self.__studenti.append(student)

    def sterge_student(self, id):
        """
            Stergem un student dupa id
        """
        noi_studenti = []
        for student in self.__studenti:
            if student.get_studentID() != id:
                noi_studenti.append(student)
        self.__studenti = noi_studenti

    def modifica_student(self, id, nume_nou, grup_nou):
        """
            Modificam studentul identificat dupa id
        """
        noi_studenti = []
        for student in self.__studenti:
            if student.get_studentID() == id:
                student.set_nume(nume_nou)
                student.set_grup(grup_nou)
            noi_studenti.append(student)
        self.__studenti = noi_studenti

    def cauta_ID(self, id):
        """
            Cautam sa vedem daca id-ul apartine deja unui student
        """
        return cautaStudent(self.__studenti, id, len(self.__studenti))
    
    def returneaza_studenti(self):
        """
            Returnam lista tuturor studentilor
        """
        return self.__studenti
    
    def __eq__(self, other):
        return self.__studenti == other.__studenti