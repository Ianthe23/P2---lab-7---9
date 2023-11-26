from domain.entitati import studenti, probleme, note
from domain.validatori import StudentValidator, ProblemaValidator, NotaValidator
from repository.studenti_repo import OperatiiStudenti
from repository.probleme_repo import OperatiiProbleme
from repository.note_repo import OperatiiNote
from service.studenti_srv import StudentService
from service.probleme_srv import ProblemaService
from service.note_srv import NoteService
from ui.console import console

Student = StudentService(OperatiiStudenti(), StudentValidator())
Problema = ProblemaService(OperatiiProbleme(), ProblemaValidator())
Note = NoteService(OperatiiNote(), NotaValidator())

ui = console(Student, Problema, Note)

ui.show_ui()