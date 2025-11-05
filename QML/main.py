import sys, random
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtCore import QObject, Slot, Signal


# Connects to to the QML file
class Backend(QObject):
    right_or_wrong = Signal(bool, str)
    error_popup = Signal(bool, str)

    def __init__(self, engine, words_to_guess: list[str]):
        super().__init__()
        self.engine = engine
        self.words_to_guess = words_to_guess


    @Slot()
    def show_content(self):

        root = self.engine.rootObjects()[0]
        # start_button: QObject = root.findChild(QObject, "start_button") # uses the objectName: "start_button" from test.qml
        tries_lbl: QObject = root.findChild(QObject, "tries_lbl") # uses the objectName: "tries_lbl" from test.qml

        # start_button.setParent(None) 
        # start_button.deleteLater() 

        tries_lbl.setProperty("visible", True)
        column: QObject = root.findChild(QObject, "contentColumn")
        column.setProperty("visible", True)


    @Slot()
    def create_blanks(self):
        root = self.engine.rootObjects()[0]
        blank_lbl: QObject = root.findChild(QObject, "blank_lbl")
        self.chosen_word: str = random.choice(self.words_to_guess)

        # creating the blanks to be displayed

        blanks_list: list[str] = list(self.chosen_word)

        for index in range(len(blanks_list)):
            blanks_list[index] = "_"

        self.blanked_word: str = " ".join(blanks_list) # The underlines can't be distinguished if there is no space in between
        blank_lbl.setProperty("text", self.blanked_word)
    

    @Slot()
    def generate_tries(self):
        root = self.engine.rootObjects()[0]
        tries_lbl: QObject = root.findChild(QObject, "tries_lbl")

        letters: list[str] = []
        for letter in self.chosen_word:
            if letter not in letters:
                letters.append(letter)

        self.tries_left: int = len(letters) - 2

        tries_lbl.setProperty("text", f"Tries Left: {self.tries_left}")


    @Slot( str )
    def users_answer_from_TF(self, users_answer: str):
        root = self.engine.rootObjects()[0]
        users_answer_TF: QObject = root.findChild(QObject, "users_answer_TF")

        users_answer_TF.setProperty("text", "")
        if ( users_answer.isalpha() ): 
            self.check_answer(users_answer)

        else :
            self.error_popup.emit(True, "Your guess must be a letter only")
        

    @Slot()
    def users_answer_from_btn(self):
        root = self.engine.rootObjects()[0]
        users_answer_TF: QObject = root.findChild(QObject, "users_answer_TF")

        users_answer: str = users_answer_TF.property("text")
        users_answer_TF.setProperty("text", "")

        if ( users_answer.isalpha() ): 

            self.check_answer(users_answer)

        else :
            self.error_popup.emit(True, "Your guess must be a letter only")


    @Slot()
    def check_answer(self, answer: str):
        root = self.engine.rootObjects()[0]
        blank_lbl = root.findChild(QObject, "blank_lbl")
        tries_lbl = root.findChild(QObject, "tries_lbl")

        if ( self.tries_left == 0 and len(answer) == 1 and answer != self.chosen_word ):
            self.error_popup.emit(True, "You ran out of tries")

        else :
            if ( len(answer) == 1 ):

                # single letters
                if ( answer in self.chosen_word):
                        temp_chosen_word: list[str] = list(self.chosen_word)
                        temp_blanks: list[str] = list(self.blanked_word)

                        while answer in temp_chosen_word:
                            index_for_word: int = temp_chosen_word.index(answer)
                            index_for_blanks: int = index_for_word * 2
                            temp_blanks[index_for_blanks] = answer
                            temp_chosen_word[index_for_word] = "_" 

                        self.blanked_word = "".join(temp_blanks)
                        blank_lbl.setProperty("text", self.blanked_word)

                self.tries_left -= 1
                tries_lbl.setProperty("text", f"Tries Left: {self.tries_left}")

            else: 

                # words
                if ( answer == self.chosen_word):
                    self.right_or_wrong.emit(True, self.chosen_word)

                else:
                    self.right_or_wrong.emit(False, "")



        
        

# <---------What runs the app------------->
app = QGuiApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.addImportPath(sys.path[0])

words: list[str] = ["activate", "expansion", "pepper", "dance", "exact"]

backend = Backend(engine, words)
engine.rootContext().setContextProperty("backend", backend)


# Load QML file
engine.load("main.qml")


if not engine.rootObjects():
    sys.exit(-1)

sys.exit(app.exec())