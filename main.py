from domain.entitati import studenti, probleme, note
from domain.validatori import StudentValidator, ProblemaValidator, NotaValidator
from repository.studenti_repo import OperatiiStudenti, OperatiiStudentiFile
from repository.probleme_repo import OperatiiProbleme, OperatiiProblemeFile
from repository.note_repo import OperatiiNote, OperatiiNoteFile
from service.studenti_srv import StudentService
from service.probleme_srv import ProblemaService
from service.note_srv import NoteService
from ui.console import console

Student = StudentService(OperatiiStudentiFile("studenti.txt"), StudentValidator())
Problema = ProblemaService(OperatiiProblemeFile("probleme.txt"), ProblemaValidator())
Note = NoteService(OperatiiNoteFile("note.txt"), NotaValidator(), Student)

ui = console(Student, Problema, Note)

ui.show_ui()