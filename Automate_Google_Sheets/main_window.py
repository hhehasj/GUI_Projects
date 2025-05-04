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
        self.setMinimumSize(500, 250)

        # LAYOUT
        self.main_layout = Widgets.QHBoxLayout(self)

        # Tabs
        self.tab_widget = Widgets.QTabWidget(self)
        self.main_layout.addWidget(self.tab_widget)
        self.tab_widget.addTab(Tab1(), "Frame 1")
        self.tab_widget.addTab(AttendanceTab(), "Attendance")
        self.tab_widget.addTab(TestimonyTab(), "Testimony")
        self.tab_widget.addTab(DiscussionTab(), "Discussion")


class Tab1(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)

        self.frame_layout.addWidget(self.Frame1())
        self.frame_layout.addWidget(self.Frame2())

    class Frame1(Widgets.QFrame):

        def __init__(self):
            super().__init__()

            self.frames_layout = Widgets.QVBoxLayout(self)
            self.others_frame = Widgets.QGroupBox("Extras")
            self.others_layout = Widgets.QFormLayout()
            self.frames_layout.addWidget(self.others_frame)
            self.others_frame.setLayout(self.others_layout)
            self.attendance_frame = Widgets.QFrame()
            self.frames_layout.addWidget(self.attendance_frame)

            self.setStyleSheet("""
                QLabel {
                    font-family: Comic Sans MS;
                    font-size: 15px;
                    font-weight: bold;
                    letter-spacing: 2px;
                }
                
                QFrame {
                    border-width: 1px;
                    border-style: solid;
                }
                
                QGroupBox {
                   font-weight: bold; 
                   font-size: 13px;
                   font-family: Comic Sans MS;
                }
                
                QComboBox {
                    font-family: Comic Sans MS;
                    font-size: 18px;
                    font-weight: bold;
                    padding-left: 5px;
                }
                
                QLineEdit#offering {
                    font-family: Comic Sans MS;
                    font-size: 18px;
                    font-weight: bold;
                    padding-left: 5px;
                }
                
                QLineEdit#lesson_title {
                    font-family: Comic Sans MS;
                    font-size: 15px;
                    font-weight: bold;
                    padding-left: 5px;
                }
            """)

            # WIDGETS of self.others_frame
            self.lg_leader = Widgets.QComboBox()
            self.lg_leader.addItems(["Ate Bondz", "Kuya Elisha"])

            self.offering = Widgets.QLineEdit()
            self.lesson_title = Widgets.QLineEdit()
            self.offering.setObjectName("offering")
            self.lesson_title.setObjectName("lesson_title")

            self.others_layout.addRow("LG Leader", self.lg_leader)
            self.others_layout.addRow("Offering", self.offering)
            self.others_layout.addRow("Lesson Title", self.lesson_title)

            self.others_layout.setVerticalSpacing(15)
            self.others_frame.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)

    class Frame2(Widgets.QFrame):
        def __init__(self):
            super().__init__()

            self.frame_layout = Widgets.QVBoxLayout()
            self.setLayout(self.frame_layout)
            self.frame_layout.addLayout(self.Time_Layout())
            self.frame_layout.addLayout(self.Date_Layout())

        class Time_Layout(Widgets.QHBoxLayout):
            def __init__(self):
                super().__init__()

                # FONT
                self.font = Label_Font()
                self.time_started_layout = Widgets.QVBoxLayout()
                self.addLayout(self.time_started_layout)
                self.time_ended_layout = Widgets.QVBoxLayout()
                self.addLayout(self.time_ended_layout)

                # WIDGETS
                self.time_started_lbl = Widgets.QLabel("Time Started")
                self.time_started_lbl.setFont(self.font)
                self.time_started_lbl.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)
                self.time_started_lbl.setFrameShape(Widgets.QFrame.Shape.Box)
                self.time_started_lbl.setFrameShadow(Widgets.QFrame.Shadow.Plain)

                self.time_started = Widgets.QTimeEdit()

                self.time_ended_lbl = Widgets.QLabel("Time Ended")
                self.time_ended_lbl.setFont(self.font)
                self.time_ended_lbl.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)
                self.time_ended_lbl.setFrameShape(Widgets.QFrame.Shape.Box)
                self.time_ended_lbl.setFrameShadow(Widgets.QFrame.Shadow.Plain)

                self.time_ended = Widgets.QTimeEdit()

                self.time_started_layout.addWidget(self.time_started_lbl)
                self.time_started_layout.addWidget(self.time_started)
                self.time_ended_layout.addWidget(self.time_ended_lbl)
                self.time_ended_layout.addWidget(self.time_ended)

        class Date_Layout(Widgets.QVBoxLayout):
            def __init__(self):
                super().__init__()

                # FONT
                self.font = Label_Font()

                # WIDGETS
                self.calendar_lbl = Widgets.QLabel("Date")
                self.calendar_lbl.setFont(self.font)
                self.calendar_lbl.setAlignment(Core.Qt.AlignmentFlag.AlignCenter)

                self.calendar = Widgets.QCalendarWidget()

                self.addWidget(self.calendar_lbl)
                self.addWidget(self.calendar)


class AttendanceTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)
        self.setLayout(self.frame_layout)


class TestimonyTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)
        self.setLayout(self.frame_layout)

        # WIDGETS
        self.testimony = Widgets.QLineEdit()

        # Adding widgets to the layout
        self.frame_layout.addWidget(self.testimony)


class DiscussionTab(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)
        self.setLayout(self.frame_layout)

        # WIDGETS
        self.discussion = Widgets.QLineEdit()

        # Adding widgets to the layout
        self.frame_layout.addWidget(self.discussion)


class Label_Font(Gui.QFont):
    def __init__(self):
        super().__init__()

        self.setFamily("Arial")
        self.setPointSize(15)
        self.setWeight(Gui.QFont.Weight.ExtraBold)
        self.setCapitalization(Gui.QFont.Capitalization.AllUppercase)
        self.setLetterSpacing(Gui.QFont.SpacingType.PercentageSpacing, 120)


app = Widgets.QApplication([])

screen = app.primaryScreen()
size = screen.size()

window = MainWindow()
window.show()

app.exec()
