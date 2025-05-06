import sys
import PySide6.QtWidgets as Widgets
import PySide6.QtCore as Core
import PySide6.QtGui as Gui


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

        # LAYOUT
        self.main_layout = Widgets.QHBoxLayout(self)

        # Tabs
        self.tab_widget = Widgets.QTabWidget(self)
        self.main_layout.addWidget(self.tab_widget)
        self.tab_widget.addTab(Tab1(), "Frame 1")
        self.tab_widget.addTab(TestimonyTab(), "Testimony")
        self.tab_widget.addTab(DiscussionTab(), "Discussion")
        self.tab_widget.addTab(FinishTab(), "Finish")


class Tab1(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)

        self.frame_layout.addWidget(self.Frame1())
        self.frame_layout.addWidget(self.Frame2())

    class Frame1(Widgets.QFrame):

        def __init__(self):
            super().__init__()

            # Frames and Layout
            self.frames_layout = Widgets.QVBoxLayout(self)  # main frame
            self.frames_layout.setContentsMargins(0, 0, 0, 0)
            self.frames_layout.addWidget(self.Extras_GroupBox("Extras"))
            self.frames_layout.addWidget(self.Attendance_GroupBox("Attendance"))

            self.setStyleSheet("""
                QLabel {
                    font-family: Comic Sans MS;
                    font-size: 16px;
                    font-weight: normal;
                    letter-spacing: 2px;
                }
                
                QComboBox {
                    font-family: Comic Sans MS;
                    font-size: 18px;
                    font-weight: bold;
                    padding-left: 5px;
                    
                }
                
                QLineEdit {
                    font-family: Comic Sans MS;
                    font-size: 18px;
                    font-weight: bold;
                    padding-left: 5px;
                }
            """)

        class Extras_GroupBox(Widgets.QGroupBox):
            def __init__(self, title: str):
                super().__init__(title=title)

                self.extras_layout = Widgets.QFormLayout(self)

                self.lg_leader = Widgets.QComboBox()
                self.lg_leader.addItems(["Ate Bondz", "Kuya Elisha"])

                self.offering = Widgets.QLineEdit()
                self.lesson_title = Widgets.QLineEdit()
                self.offering.setObjectName("offering")
                self.lesson_title.setObjectName("lesson_title")

                self.extras_layout.addRow("LG Leader:", self.lg_leader)
                self.extras_layout.addRow("Offering:", self.offering)
                self.extras_layout.addRow("Lesson Title:", self.lesson_title)

                self.extras_layout.setVerticalSpacing(12)
                self.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)

        class Attendance_GroupBox(Widgets.QGroupBox):
            def __init__(self, title: str):
                super().__init__(title=title)

                self.attendance_layout = Widgets.QFormLayout(self)

                self.members = Widgets.QComboBox()
                self.members.addItems(["Alfred, Julienne, Aaron"])
                self.members.setObjectName('members')

                self.remove_person = Widgets.QLineEdit()
                self.members.setObjectName('remove_person')
                self.add_person = Widgets.QLineEdit()
                self.members.setObjectName('add_person')

                self.save_box = Widgets.QCheckBox("")

                self.attendance_layout.addRow('Members:', self.members)
                self.attendance_layout.addRow('Add Person:', self.remove_person)
                self.attendance_layout.addRow('Remove Person:', self.add_person)
                self.attendance_layout.addRow("Save:", self.save_box)

                self.attendance_layout.setVerticalSpacing(12)
                self.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)

    class Frame2(Widgets.QGroupBox):
        def __init__(self):
            super().__init__()

            self.frame_layout = Widgets.QVBoxLayout(self)
            self.frame_layout.addLayout(self.Time_Layout())
            self.frame_layout.addLayout(self.Date_Layout())

            self.setStyleSheet("""
                QLabel {
                    font-family: Comic Sans MS;
                    font-size: 18px;
                    font-weight: bold;
                    letter-spacing: 1px;
                }
                
                QLabel#time_started_lbl {
                    margin-top: 5px;
                }
                
                QLabel#time_ended_lbl {
                    margin-top: 5px;
                }
                
                QLabel#calendar_lbl {
                    margin-top: 8px;
                }
                
                QTimeEdit {
                    font-family: Comic Sans MS;
                    font-size: 18px;
                    font-weight: 200px;
                }
                
                QGroupBox {
                    margin-top: 8px;
                }
            """)

        class Time_Layout(Widgets.QHBoxLayout):
            def __init__(self):
                super().__init__()

                self.time_started_layout = Widgets.QVBoxLayout()
                self.addLayout(self.time_started_layout)
                self.time_ended_layout = Widgets.QVBoxLayout()
                self.addLayout(self.time_ended_layout)

                # WIDGETS
                self.time_started_lbl = Widgets.QLabel("Time Started")
                self.time_started_lbl.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)
                self.time_started_lbl.setObjectName("time_started_lbl")

                self.time_started = Widgets.QTimeEdit()

                self.time_ended_lbl = Widgets.QLabel("Time Ended")
                self.time_ended_lbl.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)
                self.time_ended_lbl.setObjectName(u"time_ended_lbl")

                self.time_ended = Widgets.QTimeEdit()

                self.time_started_layout.addWidget(self.time_started_lbl)
                self.time_started_layout.addWidget(self.time_started)
                self.time_ended_layout.addWidget(self.time_ended_lbl)
                self.time_ended_layout.addWidget(self.time_ended)

        class Date_Layout(Widgets.QVBoxLayout):
            def __init__(self):
                super().__init__()

                # WIDGETS
                self.calendar_lbl = Widgets.QLabel("Date")
                self.calendar_lbl.setObjectName("calendar_lbl")
                self.calendar_lbl.setMaximumSize(150, 250)
                self.calendar_lbl.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)

                self.calendar = Widgets.QCalendarWidget()
                self.calendar.setMaximumSize(450, 300)

                self.addWidget(self.calendar_lbl, alignment=Core.Qt.AlignmentFlag.AlignHCenter | Core.Qt.AlignmentFlag.AlignBottom)
                self.addWidget(self.calendar)


class TestimonyTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QVBoxLayout(self)
        self.setStyleSheet("""
            QFrame {
                margin: 0px 3px;
            }
            
            QLabel {
                font-family: Comic Sans MS;
                font-size: 25px;
                font-weight: bold;
            }
            
            QPlainTextEdit {
                font-family: Comic Sans MS;
                font-size: 15px;
                padding: 4px 5px;
                border: 2px solid black;
                border-radius: 10;
            }
        """)

        # WIDGETS
        self.testimony_lbl = Widgets.QLabel("TESTIMONIES:")
        self.testimony = Widgets.QPlainTextEdit()

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
                font-family: Comic Sans MS;
                font-size: 25px;
                font-weight: bold;
            }
            
            QPlainTextEdit {
                font-family: Comic Sans MS;
                font-size: 15px;
                padding: 4px 5px;
                border: 2px solid black;
                border-radius: 10;
            }
        """)

        # WIDGETS
        self.discussion_lbl = Widgets.QLabel("DISCUSSION:")
        self.discussion = Widgets.QPlainTextEdit()

        # Adding widgets to the layout
        self.frame_layout.addWidget(self.discussion_lbl)
        self.frame_layout.addWidget(self.discussion)


class FinishTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)
        self.setStyleSheet("""
        QPushButton#finish_btn {
            font-family: Comic Sans MS;
            font-size: 35px;
            border: 3px solid black;
            border-radius: 15px;
            padding: 5px 10px;
        }
        QPushButton#finish_btn:hover {
            background-color: #f4f4f4;    
        }
        
        QPushButton#finish_btn:pressed {
            background-color: #c7c7c7;
        }
        
        """)

        # WIDGETS
        self.finish_btn = Widgets.QPushButton("FINISH", self)
        self.finish_btn.setObjectName("finish_btn")

        self.frame_layout.addWidget(self.finish_btn, alignment=Core.Qt.AlignmentFlag.AlignCenter)


app = Widgets.QApplication([])

screen = app.primaryScreen()
size = screen.size()

window = MainWindow()
window.show()

app.exec()
