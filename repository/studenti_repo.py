from domain.entitati import Studenti
import os

def cautaStudent(lista, id, n):
    if n < 0:
        raise ValueError("Id-ul nu a fost gasit!")
    if int(lista[n - 1].get_studentID()) == id:
        return lista[n - 1]
    return cautaStudent(lista, id, n - 1)

def adaugareValida(lista, id, n):
    if n < 0:
        return True
    if int(lista[n - 1].get_studentID()) == id:
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
        student = Studenti(nou_student.get_studentID(), nou_student.get_nume(), nou_student.get_grup())
        if len(self.__studenti) > 0:
            if adaugareValida(self.__studenti, student.get_studentID(), len(self.__studenti)):
                self.__studenti.append(student)
        else:
            self.__studenti.append(student)

    def sterge_student(self, id): # -> O(len(self.__studenti))
        """
            Stergem un student dupa id
        """
        noi_studenti = []
        for student in self.__studenti:
            if int(student.get_studentID()) != id:
                noi_studenti.append(student)
        self.__studenti = noi_studenti

    def modifica_student(self, id, nume_nou, grup_nou):
        """
            Modificam studentul identificat dupa id
        """
        noi_studenti = []
        for student in self.__studenti:
            if int(student.get_studentID()) == id:
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
    

class OperatiiStudentiFile(OperatiiStudenti):
    
    def __init__(self, filename):
        """
            Initializam repo-ul cu numele fisierului
        """
        OperatiiStudenti.__init__(self)
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
                student_ID, nume, grup = [elem.strip() for elem in line.split(", ")]
                student = Studenti(student_ID, nume, grup)
                OperatiiStudenti.adauga_student(self, student)

    def __save_in_file(self):
        """
            Salvam datele in fisier
        """
        with open(self.__filename, "w") as f:
            toti_studentii = OperatiiStudenti.returneaza_studenti(self)
            for student in toti_studentii:
                student_citit = str(student.get_studentID()) + ", " + str(student.get_nume()) + ", " + str(student.get_grup()) + "\n"
                f.write(student_citit)
        
    def adauga_student(self, student_nou):
        """
            Adaugam un student nou
        """
        OperatiiStudenti.adauga_student(self, student_nou)
        self.__save_in_file()

    def sterge_student(self, id):
        """
            Stergem un student dupa id
        """
        OperatiiStudenti.sterge_student(self, id)
        self.__save_in_file()

    def modifica_student(self, id, nume_nou, grup_nou):
        """
            Modificam un student dupa id
        """
        OperatiiStudenti.modifica_student(self, id, nume_nou, grup_nou)
        self.__save_in_file()

    def cauta_ID(self, id):
        """
            Returnam un student dupa id
        """
        return OperatiiStudenti.cauta_ID(self, id)
    
    def returneaza_studenti(self):
        """
            Returnam toti studentii
        """
        return OperatiiStudenti.returneaza_studenti(self)
    
    def __eq__(self, other):
        """
            Suprascrie metoda eq
        """
        return OperatiiStudenti.__eq__(self, other)
    




