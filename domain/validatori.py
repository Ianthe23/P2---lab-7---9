from domain.entitati import studenti, probleme
from utils.functions import verificare_float, validare_data

class StudentValidator: 
    def valideaza_studentul(self, student):
        erori = []
        if student.get_studentID() < 0:
            erori.append("Id-ul studentului nu poate fi negativ!")
        if student.get_nume() == "":
            erori.append("Numele studentului nu poate fi vid!")
        if student.get_grup() < 0:
            erori.append("Grupul studentului nu poate fi negativ!")
        if len(erori) > 0:
            raise ValueError(erori)
        
class ProblemaValidator:
    def valideaza_problema(self, problema):
        erori = []
        if not verificare_float(problema.get_nrlab_nrpb()):
            erori.append("Nr lab si nr pb trebuie sa fie rational!")
        if problema.get_descriere() == "":
            erori.append("Descrierea problemei nu poate fi vid!")
        if not validare_data(problema.get_deadline()):
            erori.append("Deadline-ul nu a fost introdus corect!")
        if len(erori) > 0:
            raise ValueError(erori)

class NotaValidator:
    def valideaza_nota(self, note):
        erori = []
        if note.get_id_student() < 0:
            erori.append("Id-ul studentului nu poate fi negativ!")
        if not verificare_float(note.get_id_problema()):
            erori.append("Nr lab si nr pb trebuie sa fie rational!")
        if note.get_nota() < 0:
            erori.append("Nota nu poate fi negativa!")
        if len(erori) > 0:
            raise ValueError(erori)
        
