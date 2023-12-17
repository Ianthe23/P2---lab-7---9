from domain.entitati import Note
from domain.validatori import NotaValidator
from repository.studenti_repo import OperatiiStudenti
from repository.probleme_repo import OperatiiProbleme
from repository.note_repo import OperatiiNoteFile, OperatiiNote
from service.studenti_srv import StudentService
from utils.functions import quicksort_2, quicksort_1, gnomesort

class NoteService:
    def __init__(self, repo, validator, student_srv):
        """
            Initializam clasa
        """
        self.__repo = repo
        self.__validator = validator
        self.__student_srv = student_srv

    def add_nota(self, id1, id2, nota_data):
        """
            Adaugam o nota unui student pe o problema
        """
        nota = Note(id1, id2, nota_data)
        self.__validator.valideaza_nota(nota)
        self.__repo.adauga_nota(nota)
        return nota

    def delete_nota(self, id1, id2):
        """
            Stergem o nota
        """
        self.__repo.sterge_nota(id1, id2)

    def modify_nota(self, id1, id2, nota_noua):
        notaNoua = Note(id1, id2, nota_noua)
        self.__validator.valideaza_nota(notaNoua)
        self.__repo.modifica_nota(id1, id2, nota_noua)
        return notaNoua
    
    def creeare_raport(self):
        lista_note = self.__repo.returneaza_note()
        raport = []
        for nota in lista_note:
            student = self.__student_srv.search_id(nota.get_id_student())
            raport.append([nota.get_id_student(), student.get_nume(), nota.get_id_problema(), nota.get_nota()])
        
        return raport

    def raport_crescator_nume(self):
        raport = self.creeare_raport()
    
        raport_sortat = quicksort_2(raport, key = lambda x: x[1])
        return raport_sortat
    
    def raport_crescator_nota(self):
        raport = self.creeare_raport()
        
        raport_sortat = quicksort_2(raport, key = lambda x: x[3])
        return raport_sortat
    
    def raport_medie_mai_mica_decat_5(self):
        raport = self.creeare_raport()

        raport_sortat = gnomesort(raport, key = lambda x: x[0])

        medie = 0
        index = 0
        ct = 1

        while(index != len(raport_sortat) - 1):
            if raport_sortat[index][0] == raport_sortat[index + 1][0] and int(raport_sortat[index][2]) == int(raport_sortat[index + 1][2]):
                medie += raport_sortat[index][3]
                ct += 1
            else:
                medie += raport_sortat[index][3]
                for index1 in range(index - ct + 1, index + 1):
                    raport_sortat[index1].extend([medie / ct])
                medie = 0
                ct = 1
            index += 1
        if raport_sortat[index][0] == raport_sortat[index - 1][0] and int(raport_sortat[index][2]) == int(raport_sortat[index - 1][2]):
            medie += raport_sortat[index][3]
            for index1 in range(index - ct + 1, index + 1):
                    raport_sortat[index1].extend([medie / ct])
        else:
            raport_sortat[index].extend([raport_sortat[index][3]])
        return raport_sortat

    def raport_primii_10_studenti(self):
        raport = self.creeare_raport()

        raport_sortat = gnomesort(raport, key = lambda x: (x[3], x[1]))
        return raport_sortat


    def get_note(self):
        """
            Returnam toate notele
        """
        return self.__repo.returneaza_note()