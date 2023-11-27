import random
from termcolor import colored

def printOptiuni(opt):
    """
        Afisam celelalte optiuni
    """
    print("Alegeti ce fel de operatie doriti sa efectuati:")
    if opt == 'A':
        print("   1) pentru a adauga un student;")
        print("   2) pentru a adauga o problema.\n")
    elif opt == 'B':
        print("   1) pentru a sterge un student;")
        print("   2) pentru a sterge o problema.\n")
    elif opt == 'C':
        print("   1) pentru a modifica datele unui student;")
        print("   2) pentru a modifica datele unei probleme.\n")
    elif opt == 'D':
        print("   1) pentru a adauga random n studenti;")
        print("   2) pentru a adauga random n probleme.\n")
    elif opt == 'E':
        print("   1) pentru a cauta un student dupa ID;")
        print("   2) pentru a cauta o problema dupa nr. lab si nr. pb.\n")
    elif opt == 'I':
        print("   1) pentru a ordona notele dupa numele studentilor;")
        print("   2) pentru a ordona notele dupa nota.\n")
    else:
        print ("Comanda invalida\n")

def printMeniu():
    """
        Afisam optiunile meniului
    """
    print("Va rugam sa alegeti o optiune de mai jos: ")
    print("   A) adaugati un student sau o problema in lista;")
    print("   B) stergeti un student sau o problema din lista;")
    print("   C) modificati datele unui student sau unei probleme;")
    print("   D) adaugati random studenti sau probleme;")
    print("   E) cautati un student sau o problema dupa identificator;")
    print("-----------------------------------------------------------")
    print("   F) adaugati o nota unui student pe o problema;")
    print("   G) sterge o nota a unui student pe o problema;")
    print("   H) modificati nota unui student de la o anumita problema;")
    print("-----------------------------------------------------------")
    print("   I) creeati un raport pentru notele studentilor;")
    print("   J) creeati un raport pentru mediile mai mici decat 5 ale studentilor;")
    print("   K) creeati un raport cu notele primilor 30% studenti ordonati dupa nota;")
    print("   X) iesiti din aplicatie.\n")


class console:
    def __init__(self, srv1, srv2, srv3):
        """
            Initializam consola pentru a lucra cu controllerul GRASP
        """
        self.__srv1 = srv1
        self.__srv2 = srv2
        self.__srv3 = srv3

    #zona studentilor
    def __add_student(self):
        """
            Adaugam un student nou
        """
        student_id = int(input("Introduceti id-ul studentului: "))
        nume = input("Introduceti numele studentului: ")
        grup = int(input("Introduceti grupul studentului: "))

        try:
            student = self.__srv1.add_student(student_id, nume, grup)
        except ValueError as ve:
            print(ve)

    def __delete_student(self):
        """
            Stergem un student dupa id
        """
        try:
            student_id = int(input("Introduceti id-ul studentului de sters: "))
            student = self.__srv1.search_id(student_id)
            if not student:
                raise ValueError("Id-ul nu este valid!")
            self.__srv1.delete_student(student_id)
        except ValueError as ve:
            print(ve)

    def __modify_student(self):
        """
            Modificam un student dupa id
        """
        try:
            student_id = int(input("Introduceti id-ul studentului de modificat: "))
            student = self.__srv1.search_id(student_id)
            if not student:
                raise ValueError("Id-ul nu este valid!")
            nume = input("Introduceti numele nou: ")
            grup = int(input("Introduceti grupul nou: "))
            self.__srv1.modify_student(student_id, nume, grup)
        except ValueError as ve:
            print(ve)

    def __search_id_student(self):
        """
            Caut student dupa id
        """
        try:
            student_id = int(input("Introduceti id-ul studentului de cautat: "))
            student = self.__srv1.search_id(student_id)
            return student
        except ValueError as ve:
            print(ve)

    def __add_random_student(self):
        """
            Adaugam random n filme
        """
        try:
            number = random.randint(1, 10)
            self.__srv1.add_random_studenti(number)
            st = "Au fost adaugati " + str(number) + " studenti"
            print(colored(st, "green"))
        except ValueError as ve:
            print("Operatiunea a esuat.")            
        

    def __show_all_studenti(self):
        return self.__srv1.get_studenti()

    #zona problemelor
    def __add_problema(self):
        """
            Adaugam o problema noua
        """
        nrlab_nrpb = float(input("Introduceti nr. lab. si nr. pb.: "))
        descriere = input("Introduceti descrierea problemei: ")
        deadline = input("Introduceti deadline-ul problemei: ")

        try:
            problema = self.__srv2.add_problema(nrlab_nrpb, descriere, deadline)
        except ValueError as ve:
            print(ve)

    def __delete_problema(self):
        """
            Stergem o problema dupa nr lab si nr pb
        """

        try:
            nrlab_nrpb = float(input("Introduceti nr.lab si nr. pb. de sters: "))
            problema = self.__srv2.search_nrlab_nrpb(nrlab_nrpb)
            if not problema:
                raise ValueError("Nr. lab si nr. pb nu sunt valide!")
            self.__srv2.delete_problema(nrlab_nrpb)
        except ValueError as ve:
            print(ve)

    def __modify_problema(self):
        try:
            nrlab_nrpb = float(input("Introduceti nr.lab si nr. pb. de modificat: "))
            problema = self.__srv2.search_nrlab_nrpb(nrlab_nrpb)
            if not problema:
                raise ValueError("Nr. lab si nr. pb nu sunt valide!")
            descriere = input("Introduceti descrierea noua: ")
            deadline = input("Introduceti deadline-ul nou: ")
            self.__srv2.modify_problema(nrlab_nrpb, descriere, deadline)
        except ValueError as ve:
            print(ve)

    def __search_nrlab_nrpb_problema(self):
        """
            Cautam problema dupa nr lab si nr pb
        """
        try:
            nrlab_nrpb = float(input("Introduceti nr.lab si nr. pb. de cautat: "))
            problema = self.__srv2.search_nrlab_nrpb(nrlab_nrpb)
            return problema
        except ValueError as ve:
            print(ve)

    def __add_random_problema(self):
        """
            Adaugam random n filme
        """
        try:
            number = random.randint(1, 10)
            self.__srv2.add_random_probleme(number)
            st = "Au fost adaugate " + str(number) + " probleme"
            print(colored(st, "green"))
        except ValueError as ve:
            print("Operatiunea a esuat.")    

    def __show_all_probleme(self):
        return self.__srv2.get_probleme()
    
    #zona notelor
    def __note(self):
        """
            Implementam interfata utilizator pentru note
        """
        try:
            id1 = int(input("Introduceti id-ul studentului: "))
            student = self.__srv1.search_id(id1)
            if student:
                print("\n")
                print("Acestea sunt problemele disponibile: ")
                for elem in self.__srv2.get_probleme():
                    print(elem)
                print("\n")
                id2 = float(input("Introduceti nr. lab. si nr. pb.: "))
                problema = self.__srv2.search_nrlab_nrpb(id2)
                if problema:
                    nota = float(input("Introduceti nota: "))
                    self.__srv3.add_nota(id1, id2, nota)
        except ValueError as ve:
            print(ve)

    def __sterge_nota(self):
        """
            Stergem nota unui student
        """
        try:
            id1 = int(input("Introduceti id-ul studentului: "))
            student = self.__srv1.search_id(id1)
            if student:
                print("\n")
                print("Acestea sunt problemele disponibile: ")
                for elem in self.__srv2.get_probleme():
                    print(elem)
                print("\n")
                id2 = float(input("Introduceti nr. lab. si nr. pb.: "))
                problema = self.__srv2.search_nrlab_nrpb(id2)
                if problema:
                    self.__srv3.delete_nota(id1, id2)
        except ValueError as ve:
            print(ve)
    
    def __modifica_nota(self):
        """
            Modificam nota unui student
        """
        try:
            id1 = int(input("Introduceti id-ul studentului: "))
            student = self.__srv1.search_id(id1)
            if student:
                print("\n")
                print("Acestea sunt problemele disponibile: ")
                for elem in self.__srv2.get_probleme():
                    print(elem)
                print("\n")
                id2 = float(input("Introduceti nr. lab. si nr. pb.: "))
                problema = self.__srv2.search_nrlab_nrpb(id2)
                if problema:
                    nota_noua = float(input("Introduceti noua nota: "))
                    self.__srv3.modify_nota(id1, id2, nota_noua)
        except ValueError as ve:
            print(ve)

    #zona rapoartelor
    def __raport_crescator_nume(self):
        """
            Generam raportul ordonat crescator
        """
        lista_note = self.__srv3.get_note()
        lista_completa = []
        
        #creeam lista completa cu numele studentilor
        for index in range(len(lista_note)):
            student = self.__srv1.search_id(lista_note[index][0])
            lista_completa.append([lista_note[index][0], student.get_nume(), lista_note[index][1], lista_note[index][2]])

        #ordonam dupa nume lista
        lista_completa_sortata = sorted(lista_completa, key=lambda x: x[1])

        #afisam raportul
        underlined_string = "   "+ "\033[4m" + "Raport privind notele studentilor ordonate dupa nume" + "\033[0m"
        print("\n")
        print(colored(underlined_string, "yellow"))
        print("\n")
        for elem in lista_completa_sortata:
            print(colored("id:", "blue"), end = " ")
            print(elem[0], end = "  ")
            print(colored("nume:", "green"), end = " ")
            print(elem[1], end = "  ")
            print(colored("nr lab si nr pb:", "red"), end = " ")
            print(elem[2], end = "  ")
            print(colored("nota:", "magenta"), end = " ")
            print(elem[3])
    
    def __raport_crescator_nota(self):
        """
            Generam raportul ordonat crescator
        """
        lista_note = self.__srv3.get_note()
        lista_completa = []
        
        #creeam lista completa cu numele studentilor
        for index in range(len(lista_note)):
            student = self.__srv1.search_id(lista_note[index][0])
            lista_completa.append([lista_note[index][0], student.get_nume(), lista_note[index][1], lista_note[index][2]])

        #ordonam dupa nume lista
        lista_completa_sortata = sorted(lista_completa, key=lambda x: x[3])

        #afisam raportul
        underlined_string = "   "+ "\033[4m" + "Raport privind notele studentilor ordonate crescator" + "\033[0m"
        print("\n")
        print(colored(underlined_string, "yellow"))
        print("\n")
        for elem in lista_completa_sortata:
            print(colored("id:", "blue"), end = " ")
            print(elem[0], end = "  ")
            print(colored("nume:", "green"), end = " ")
            print(elem[1], end = "  ")
            print(colored("nr lab si nr pb:", "red"), end = " ")
            print(elem[2], end = "  ")
            print(colored("nota:", "magenta"), end = " ")
            print(elem[3])

    def __raport_nota_mai_mica_de_5(self):
        """
            Generam raportul ordonat crescator
        """
        lista_note = self.__srv3.get_note()
        lista_completa = []
        
        #creeam lista completa cu numele studentilor
        for index in range(len(lista_note)):
            student = self.__srv1.search_id(lista_note[index][0])
            lista_completa.append([lista_note[index][0], student.get_nume(), lista_note[index][1], lista_note[index][2]])
        
        #sortam lista completa dupa id-ul acestora
        lista_completa_sortata = sorted(lista_completa, key=lambda x: (x[0], x[2]))
        lista_medie = []
        medie = 0
        ct = 1
        index = 0

        #calculam media pe fiecare laborator al fiecarui student
        while(index != len(lista_completa_sortata) - 1):
            if lista_completa_sortata[index][0] == lista_completa_sortata[index + 1][0] and int(lista_completa_sortata[index][2]) == int(lista_completa_sortata[index + 1][2]):
                medie += lista_completa_sortata[index][3]
                ct += 1
            else:
                medie += lista_completa_sortata[index][3]
                lista_medie.append([lista_completa_sortata[index][1], medie / ct, int(lista_completa_sortata[index][2])])
                medie = 0
                ct = 1
            index += 1
        #verificam daca ultimul student are acelasi id si laborator cu cel de dinainte
        if lista_completa_sortata[index][0] == lista_completa_sortata[index - 1][0] and int(lista_completa_sortata[index][2]) == int(lista_completa_sortata[index - 1][2]):
            medie += lista_completa_sortata[index][3]
            lista_medie.append([lista_completa_sortata[index][1], medie / ct, int(lista_completa_sortata[index][2])])
        else:
            lista_medie.append([lista_completa_sortata[index][1], lista_completa_sortata[index][3], int(lista_completa_sortata[index][2])])
    
        #afisam raportul
        underlined_string = "   "+ "\033[4m" + "Raport privind mediile studentilor mai mici decat 5" + "\033[0m"
        print("\n")
        print(colored(underlined_string, "yellow"))
        print("\n")
        for elem in lista_medie:
            if elem[1] < 5:  
                print(colored("nume:", "blue"), end = " ")
                print(elem[0], end = "  ")
                print(colored("medie:", "green"), end = " ")
                print(elem[1], end = "  ")
                print(colored("laborator:", "red"), end = " ")
                print(elem[2])

            

    def __raport_primii_30_studenti(self):
        lista_note = self.__srv3.get_note()
        lista_completa = []
        
        #creeam lista completa cu numele studentilor
        for index in range(len(lista_note)):
            student = self.__srv1.search_id(lista_note[index][0])
            lista_completa.append([lista_note[index][0], student.get_nume(), lista_note[index][1], lista_note[index][2]])
        
        #ordonez lista dupa nota si dupa aceea dupa nume
        lista_completa_sortata = sorted(lista_completa, key=lambda x: (x[3], x[1]))
        
        #afisez raportul
        underlined_string = "   "+ "\033[4m" + "Raport privind notele primilor 30% studenti ordonati dupa nota" + "\033[0m"
        print("\n")
        print(colored(underlined_string, "yellow"))
        print("\n")
        for index in range(int(len(lista_completa_sortata) / 3)):
            print(colored("id:", "blue"), end = " ")
            print(lista_completa_sortata[index][0], end = "  ")
            print(colored("nume:", "green"), end = " ")
            print(lista_completa_sortata[index][1], end = "  ")
            print(colored("nr lab si nr pb:", "red"), end = " ")
            print(lista_completa_sortata[index][2], end = "  ")
            print(colored("nota:", "magenta"), end = " ")
            print(lista_completa_sortata[index][3])
            
    def __show_all_note(self):
        return self.__srv3.get_note()



    
    def show_ui(self):
        exit = False
        while not(exit):
            print("\n")
            print("Lista de studenti: ", self.__show_all_studenti())
            print("Lista de probleme: ", self.__show_all_probleme())
            print("Lista de note: ", self.__show_all_note())
            print("\n")
            printMeniu()
            optiune = input("Introduceti optiunea: ").strip()
            if optiune == 'X':
                print("\nLa revedere!")
                exit = True
            else:
                if optiune == 'A':
                    printOptiuni(optiune)
                    cerinta = input("Introduceti cerinta: ").strip()  
                    if cerinta == '1':
                        self.__add_student()
                    elif cerinta == '2':
                        self.__add_problema()
                    else:
                        print("Comanda invalida!\n")
                elif optiune == 'B':
                    printOptiuni(optiune)
                    cerinta = input("Introduceti cerinta: ").strip()
                    if cerinta == '1':
                        self.__delete_student()
                    elif cerinta == '2':
                        self.__delete_problema()
                    else:
                        print("Comanda invalida!\n")
                elif optiune == 'C':
                    printOptiuni(optiune)
                    cerinta = input("Introduceti cerinta: ").strip()
                    if cerinta == '1':
                        self.__modify_student()
                    elif cerinta == '2':
                        self.__modify_problema()
                    else:
                        print("Comanda invalida!\n")
                elif optiune == 'D':
                    printOptiuni(optiune)
                    cerinta = input("Introduceti cerinta: ").strip()
                    if cerinta == '1':
                        self.__add_random_student()
                    elif cerinta == '2':
                        self.__add_random_problema()
                    else:
                        print("Comanda invalida!\n")
                elif optiune == 'E':
                    printOptiuni(optiune)
                    cerinta = input("Introduceti cerinta: ").strip()
                    if cerinta == '1':
                        student = self.__search_id_student()
                        if student:
                            print(student)
                    elif cerinta == '2':
                        problema = self.__search_nrlab_nrpb_problema()
                        if student:
                            print(problema)
                    else:
                        print("Comanda invalida!\n")
                elif optiune == 'F':
                    self.__note()
                elif optiune == 'G':
                    self.__sterge_nota()
                elif optiune == 'H':
                    self.__modifica_nota()
                    
                elif optiune == 'I':
                    printOptiuni(optiune)
                    cerinta = input("Introduceti cerinta: ").strip()
                    if cerinta == '1':
                        self.__raport_crescator_nume()
                    elif cerinta == '2':
                        self.__raport_crescator_nota()
                    else:
                        print("Comanda invalida!\n")

                elif optiune == 'J':
                    self.__raport_nota_mai_mica_de_5()
                    
                elif optiune == 'K':
                    self.__raport_primii_10_studenti()
                else:
                    print("Comanda invalida!\n")
                
                






