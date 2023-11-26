from termcolor import colored

"""
    Scrieți o aplicație pentru gestiunea notelor și a problemelor de laborator pentru o disciplină.
"""

def reset_lista():
    """
        Returnam o lista goala
    """
    return []

class studenti:
    def __init__(self, studentID, nume, grup):
        """
            Construim clasa cu datele necesare studentilor
        """
        self.__studentID = studentID
        self.__nume = nume
        self.__grup = grup

        """
            Creeam functiile de get si set pt clasa
        """

    def get_studentID(self):
        return self.__studentID
        
    def get_nume(self):
        return self.__nume
        
    def get_grup(self):
        return self.__grup
        

    def set_nume(self, nume):
        self.__nume = nume

    def set_grup(self, grup):
        self.__grup = grup

    def __eq__(self, other):
        return self.__studentID == other.__studentID and self.__nume == other.__nume and self.__grup == other.__grup
    def __str__(self):
        return colored("id: ", "blue") + str(self.__studentID) + "; nume: " + str(self.__nume) + "; grup: " + str(self.__grup) + colored("; ", "red")
    def __repr__(self):
        return str(self)

class probleme:
    def __init__(self, nrlab_nrpb, descriere, deadline):
        """
            Creeam biblioteca necesara problemelor de laborator
        """
        self.__nrlab_nrpb = nrlab_nrpb
        self.__descriere = descriere
        self.__deadline = deadline

        """
            Creeam functiile de get si set pt clasa
        """
    def get_nrlab_nrpb(self):
        return self.__nrlab_nrpb

    def get_descriere(self):
        return self.__descriere

    def get_deadline(self):
        return self.__deadline
    

    def set_descriere(self, descriere):
        self.__descriere = descriere

    def set_deadline(self, deadline):
        self.__deadline = deadline

    def __eq__(self, other):
        return self.__nrlab_nrpb == other.__nrlab_nrpb and self.__descriere == other.__descriere and self.__deadline == other.__deadline
    def __str__(self):
        return colored("nrlab si pb: ", "blue") + str(self.__nrlab_nrpb) + "; descriere: " + str(self.__descriere) + "; deadline: " + str(self.__deadline) + colored("; ", "red")
    def __repr__(self):
        return str(self)

class note:
    def __init__(self, id_student, id_problema, nota):
        self.__id_student = id_student
        self.__id_problema = id_problema
        self.__nota = nota

    def get_id_student(self):
        return self.__id_student

    def get_id_problema(self):
        return self.__id_problema

    def get_nota(self):
        return self.__nota
    

    def set_id_problema(self, id_problema):
        self.__id_problema = id_problema

    def set_nota(self, nota):
        self.__nota = nota

    def __eq__(self, other):
        return self.__id_student == other.__id_student and self.__id_problema == other.__id_problema and self.__nota == other.__nota
    def __str__(self):
        return colored("id student: ", "blue") + str(self.__id_student) + "; " + colored(" id problema: ", "blue")  + str(self.__id_problema) + "; nota: " + str(self.__nota) + colored("; ", "red")
    def __repr__(self):
        return str(self)
