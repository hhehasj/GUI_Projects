import PySide6.QtWidgets as Widgets
import PySide6.QtCore as Core
from attendance_tab import AttendanceTab
from modify_worksheets import main

Data = {
    "LG Leader": "",
    "Date": "",
    "Offering": 0,
    "Attendance": "",
    "Lesson Title": "",
    "Testimonies": "",
    "Discussion": "",
    "Time Started": "",
    "Time Ended": "",
}


class MainWindow(Widgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Automate GS')
        self.windows_height: int = 500
        self.windows_width: int = 1000
        self.half_of_height: int = int((size.height() / 2) - self.windows_height / 2)
        self.half_of_width: int = int((size.width() / 2) - self.windows_width / 2)
        self.setGeometry(self.half_of_width,
                         self.half_of_height,
                         self.windows_width,
                         self.windows_height)
        self.setMaximumSize(1000, 500)

        self.main_layout = Widgets.QHBoxLayout(self)

        # Tabs
        self.tab_widget = Widgets.QTabWidget(self)
        self.main_layout.addWidget(self.tab_widget)

        self.tab_widget.addTab(AttendanceTab(), "Attendance")
        self.tab_widget.addTab(TestimonyTab(), "Testimony")
        self.tab_widget.addTab(DiscussionTab(), "Discussion")
        self.tab_widget.addTab(OtherDetailsTab(), "Other Details")


# The "widget" parameter is used to find the correct widget.
def return_ComboBox_selection(widget, selection):
    global Data

    if widget.objectName() == "lg_leader":
        Data["LG Leader"] = selection


def return_LineEdit(widget, text):
    global Data

    if widget.objectName() == "offering":
        try:
            int(text)  # To always make sure it is a number. It can't be letters or decimals.

            text = text.rstrip(" ")
            Data["Offering"] = text + " THB"

        except ValueError:
            print("Enter a number")

    if widget.objectName() == "lesson_title":
        Data["Lesson Title"] = text


def return_TimeEdit(widget, time):
    global Data

    if widget.objectName() == "time_started":
        Data["Time Started"] = time

    if widget.objectName() == "time_ended":
        Data["Time Ended"] = time


def return_PlainTextEdit(widget, content):
    global Data

    if widget.objectName() == "testimonies":
        Data["Testimonies"] = content

    if widget.objectName() == "discussion":
        Data["Discussion"] = content


class OtherDetailsTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.main_layout = Widgets.QHBoxLayout(self)

        self.details_group_box = Widgets.QGroupBox()
        self.details_gb_layout = Widgets.QFormLayout(self.details_group_box)
        self.calendar_group_box = Widgets.QGroupBox()
        self.calendar_gb_layout = Widgets.QVBoxLayout(self.calendar_group_box)

        self.main_layout.addWidget(self.details_group_box)
        self.main_layout.addWidget(self.calendar_group_box)

        self.setStyleSheet("""
            QLabel {
                font: 18px Comic Sans MS;
                font-weight: 600;
                letter-spacing: 2px;
            }
            
            QLabel#calendar_lbl {
                font: 25px Comic Sans MS;
                font-weight: 600;
                letter-spacing: 2px;
            }
               
            QComboBox {
                font: 18px Comic Sans MS;
                font-weight: bold;
                letter-spacing: 1px;
                padding-left: 5px;
                padding-top: 4px;
                padding-bottom: 3px;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: right;
                width: 25px;
                height: 25px;
                border-left: 1px solid grey;
            }
            QComboBox::down-arrow {
                width: 12px;
                height: 50px;
                image: url(icons/down_arrow.svg);
            }

            QLineEdit {
                font: 18px Comic Sans MS;
                font-weight: bold;
                letter-spacing: 1px;
                padding-left: 5px;
                padding-top: 4px;
                padding-bottom: 3px;
            }
            
            QTimeEdit {
                font: 18px Comic Sans MS;
                font-weight: bold;
                border: 1px solid #e7e7e7;
                border-radius: 5px;
                padding-left: 2px;
                padding-top: 4px;
                padding-bottom: 3px;
            }
            QTimeEdit:hover {
                background: #f5f5f5;
            }
            QTimeEdit::up-button {
                width: 25px;
                border-top-right-radius: 5px;
                border-left: 1px solid gray;
                background: #fefefe;
            }
            QTimeEdit::up-arrow {
                width: 20px;
                height: 15px;
                image: url(icons/up_arrow.svg);
            }
            QTimeEdit::down-button { 
                width: 25px;
                border-top: 1px solid gray;
                border-left: 1px solid gray;
                border-bottom-right-radius: 5px;
                background: #fefefe;
            }
            QTimeEdit::down-arrow {
                width: 20px;
                height: 15px;
                image: url(icons/down_arrow.svg);
            }
            QTimeEdit::down-button:hover, QTimeEdit::up-button:hover {
                background: #c4c4c4;
            }
            QTimeEdit::down-button:pressed, QTimeEdit::up-button:pressed {
                background: #8f8f8f;
            }
            
            QPushButton#finish_btn {
                font: 35px Comic Sans MS;
                letter-spacing: 1px;
                border: 3px solid black;
                border-radius: 15px;
                background-color: hsl(210, 100%, 70%);
                padding: 5px 10px;
            }
            QPushButton#finish_btn:hover {
                background-color: hsl(210, 80%, 50%);    
            }
            QPushButton#finish_btn:pressed {
                background-color: hsl(210, 100%, 40%);
            }
             """)

        # WIDGETS
        self.lg_leader = Widgets.QComboBox()
        self.lg_leader.setObjectName("lg_leader")
        self.lg_leader.addItems(["", "Ate Bondz", "Kuya Elisha"])
        self.lg_leader.textActivated.connect(
            lambda: return_ComboBox_selection(widget=self.lg_leader, selection=self.lg_leader.currentText()))

        self.offering = Widgets.QLineEdit()
        self.offering.setObjectName("offering")
        self.offering.textChanged.connect(
            lambda: return_LineEdit(widget=self.offering, text=self.offering.text()))

        self.lesson_title = Widgets.QLineEdit()
        self.lesson_title.setObjectName("lesson_title")
        self.lesson_title.editingFinished.connect(
            lambda: return_LineEdit(widget=self.lesson_title, text=self.lesson_title.text()))

        self.time_started = Widgets.QTimeEdit()
        self.time_started.setObjectName("time_started")
        self.time_started.setMaximumTime(Core.QTime(23, 0, 0))
        self.time_started.setMinimumTime(Core.QTime(18, 0, 0))
        self.time_started.userTimeChanged.connect(
            lambda: return_TimeEdit(widget=self.time_started, time=self.time_started.text()))

        self.time_ended = Widgets.QTimeEdit()
        self.time_ended.setObjectName("time_ended")
        self.time_ended.setMaximumTime(Core.QTime(23, 0, 0))
        self.time_ended.setMinimumTime(Core.QTime(18, 0, 0))
        self.time_ended.userTimeChanged.connect(
            lambda: return_TimeEdit(widget=self.time_ended, time=self.time_ended.text()))

        self.finish_button_frame = Widgets.QFrame()
        self.finish_button_frame.setObjectName("test_frame")
        self.FB_frame_layout = Widgets.QVBoxLayout(self.finish_button_frame)
        self.finish_btn = Widgets.QPushButton("FINISH", self)
        self.finish_btn.setObjectName("finish_btn")
        self.finish_btn.clicked.connect(self.send_data)
        self.finish_btn.setMaximumSize(165, 65)
        self.finish_btn.setMinimumSize(145, 45)

        self.calendar_lbl = Widgets.QLabel("Date")
        self.calendar_lbl.setObjectName("calendar_lbl")

        self.calendar = self.CalendarWithKeyDisplay()

        # ----------------------------------------------------------------------------------------------
        self.details_gb_layout.addRow("LG Leader:", self.lg_leader)
        self.details_gb_layout.addRow("Offering:", self.offering)
        self.details_gb_layout.addRow("Lesson Title:", self.lesson_title)
        self.details_gb_layout.addRow("Time Started:", self.time_started)
        self.details_gb_layout.addRow("Time Ended:", self.time_ended)
        self.details_gb_layout.addRow(self.finish_button_frame)
        self.FB_frame_layout.addWidget(self.finish_btn,
                                       alignment=Core.Qt.AlignmentFlag.AlignCenter,
                                       stretch=1)
        self.details_gb_layout.setVerticalSpacing(15)

        self.calendar_gb_layout.addWidget(self.calendar_lbl, alignment=Core.Qt.AlignmentFlag.AlignCenter)
        self.calendar_gb_layout.addWidget(self.calendar)

    def send_data(self):
        Data["Attendance"] = ", ".join(AttendanceTab.member_list)
        main(data=Data)

    class CalendarWithKeyDisplay(Widgets.QCalendarWidget):
        def __init__(self):
            super().__init__()

            self.setMaximumSize(450, 400)
            self.clicked.connect(self.return_clicked_date)

        def return_clicked_date(self):
            Data["Date"] = self.selectedDate().toString("MMMM dd, yyyy")

        def keyPressEvent(self, event):  # Making our own keyPressEvent
            super().keyPressEvent(event)  # Inherit from QCalendarWidget's keyPressEvent method

            # After processing the key, get the updated date
            if event.key() in (
                    Core.Qt.Key.Key_Left,
                    Core.Qt.Key.Key_Right,
                    Core.Qt.Key.Key_Up,
                    Core.Qt.Key.Key_Down,
            ):
                Data["Date"] = self.selectedDate().toString("MMMM dd, yyyy")


class TestimonyTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QVBoxLayout(self)
        self.setStyleSheet("""
            QFrame {
                margin: 0px 3px;
            }
            
            QLabel {
                font: 30px Comic Sans MS;
                font-weight: bold;
            }
            
            QPlainTextEdit {
                font: 15px Comic Sans MS;
                letter-spacing: 1px;
                padding: 4px 5px;
                border: 2px solid black;
                border-radius: 10;
            }
        """)

        # WIDGETS
        self.testimony_lbl = Widgets.QLabel("TESTIMONIES:")
        self.testimony = Widgets.QPlainTextEdit()
        self.testimony.setObjectName("testimonies")
        self.testimony.textChanged.connect(
            lambda: return_PlainTextEdit(widget=self.testimony, content=self.testimony.toPlainText()))

        # Adding widgets to the layout
        self.frame_layout.addWidget(self.testimony_lbl)
        self.frame_layout.addWidget(self.testimony)


class DiscussionTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QVBoxLayout(self)
        self.setStyleSheet("""
            QFrame {
                margin: 0px 3px;
            }
            
            QLabel {
                font: 30px Comic Sans MS;
                font-weight: bold;
            }
            
            QPlainTextEdit {
                font: 15px Comic Sans MS;
                letter-spacing: 1px;
                padding: 4px 5px;
                border: 2px solid black;
                border-radius: 10;
            }
        """)

        # WIDGETS
        self.discussion_lbl = Widgets.QLabel("DISCUSSION:")
        self.discussion = Widgets.QPlainTextEdit()
        self.discussion.setObjectName("discussion")
        self.discussion.textChanged.connect(
            lambda: return_PlainTextEdit(widget=self.discussion, content=self.discussion.toPlainText()))

        # Adding widgets to the layout
        self.frame_layout.addWidget(self.discussion_lbl)
        self.frame_layout.addWidget(self.discussion)


app = Widgets.QApplication([])

screen = app.primaryScreen()
size = screen.size()

window = MainWindow()
window.show()

app.exec()
