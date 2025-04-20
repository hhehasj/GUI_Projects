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

        # LAYOUT
        self.main_layout = Widgets.QHBoxLayout()
        self.setLayout(self.main_layout)

        # Tabs
        self.tab_widget = Widgets.QTabWidget()
        self.main_layout.addWidget(self.tab_widget)
        self.tab_widget.addTab(Tab1(), "Frame 1")
        self.tab_widget.addTab(TestimonyTab(), "Testimony")
        self.tab_widget.addTab(DiscussionTab(), "Discussion")


class Tab1(Widgets.QFrame):
    def __init__(self):
        super().__init__()

        self.frame_layout = Widgets.QHBoxLayout(self)
        self.setLayout(self.frame_layout)

        self.frame_layout.addWidget(self.Frame1())
        self.frame_layout.addWidget(self.Frame2())
        self.frame_layout.addWidget(self.Frame3())

    class Frame1(Widgets.QFrame):
        def __init__(self):
            super().__init__()

            self.frame_layout = Widgets.QVBoxLayout()
            self.setLayout(self.frame_layout)

            # WIDGETS
            self.lg_leader_lbl = Widgets.QLabel("LG Leader")
            self.lg_leader = Widgets.QComboBox()
            self.lg_leader.addItems(["Ate Bondz", "Kuya Elisha"])

            self.calendar_lbl = Widgets.QLabel("Date")
            self.calendar = Widgets.QCalendarWidget()
            self.setFixedSize(300, 200)

            # Adding widgets to the layout
            self.frame_layout.addWidget(self.lg_leader_lbl)
            self.frame_layout.addWidget(self.lg_leader)
            self.frame_layout.addWidget(self.calendar_lbl)
            self.frame_layout.addWidget(self.calendar)

    class Frame2(Widgets.QFrame):
        def __init__(self):
            super().__init__()

            self.frame_layout = Widgets.QVBoxLayout()
            self.setLayout(self.frame_layout)

            # WIDGETS
            self.time_started_lbl = Widgets.QLabel("Time Started")
            self.time_started = Widgets.QTimeEdit()

            self.time_ended_lbl = Widgets.QLabel("Time Ended")
            self.time_ended = Widgets.QTimeEdit()

            self.offering_lbl = Widgets.QLabel('Offering')
            self.offering = Widgets.QLineEdit()

            # Adding widgets to the layout
            self.frame_layout.addWidget(self.time_started_lbl)
            self.frame_layout.addWidget(self.time_started)
            self.frame_layout.addWidget(self.time_ended_lbl)
            self.frame_layout.addWidget(self.time_ended)
            self.frame_layout.addWidget(self.offering_lbl)
            self.frame_layout.addWidget(self.offering)

    class Frame3(Widgets.QFrame):
        def __init__(self):
            super().__init__()

            self.frame_layout = Widgets.QVBoxLayout()
            self.setLayout(self.frame_layout)

            # WIDGETS
            self.attendance_lbl = Widgets.QLabel("Attendance")
            self.attendance = Widgets.QComboBox()
            # self.attendance.addItems()

            self.add_person_lbl = Widgets.QLabel("Add Person")
            self.add_person = Widgets.QLineEdit()

            self.remove_person_lbl = Widgets.QLabel("Remove Person")
            self.remove_person = Widgets.QLineEdit()

            # Adding widgets to the layout
            self.frame_layout.addWidget(self.attendance_lbl)
            self.frame_layout.addWidget(self.attendance)
            self.frame_layout.addWidget(self.add_person_lbl)
            self.frame_layout.addWidget(self.add_person)
            self.frame_layout.addWidget(self.remove_person_lbl)
            self.frame_layout.addWidget(self.remove_person)


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


app = Widgets.QApplication([])

screen = app.primaryScreen()
size = screen.size()

window = MainWindow()
window.show()

app.exec()
