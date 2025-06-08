import PySide6.QtGui as Gui
import PySide6.QtWidgets as Widgets
import PySide6.QtCore as Core
from database import get_members


class AttendanceTab(Widgets.QFrame):
    member_list: list[str] = []

    def __init__(self):
        super().__init__()

        self.tabs_layout = Widgets.QVBoxLayout(self)
        self.scroll_area = Widgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.main_frame = Widgets.QFrame()
        self.scroll_area.setWidget(self.main_frame)
        self.main_frame_layout = Widgets.QVBoxLayout(self.main_frame)

        for member in get_members():
            if member is not None:
                self.main_frame_layout.addWidget(self.Members_box(member))

        self.sub_layout = Widgets.QHBoxLayout()
        self.add_person = Widgets.QLineEdit()
        self.add_person.setObjectName("add_person")
        self.add_person_btn = Widgets.QPushButton("Add Person")
        self.add_person_btn.setObjectName("add_person_btn")
        self.add_person_btn.clicked.connect(self.Add_Person)
        self.complete_btn = Widgets.QPushButton("COMPLETE")
        self.complete_btn.setObjectName("complete_btn")
        self.complete_btn.clicked.connect(self.Complete)

        # STYLESHEET of the widgets at the bottom.
        self.setStyleSheet("""
        """)

        self.tabs_layout.addWidget(self.scroll_area)
        self.tabs_layout.addLayout(self.sub_layout)
        self.sub_layout.addWidget(self.add_person)
        self.sub_layout.addWidget(self.add_person_btn)
        self.sub_layout.addWidget(self.complete_btn)

    class Members_box(Widgets.QFrame):
        def __init__(self, name: str):
            super().__init__()

            # LAYOUT
            self.members_layout = Widgets.QHBoxLayout(self)
            self.members_layout.setContentsMargins(0, 0, 0, 0)
            self.setObjectName("main_frame")
            self.setMaximumSize(935, 80)
            self.setStyleSheet("""
                QFrame#main_frame {
                    border: 2px solid black;
                    border-radius: 10px;
                    margin: 5px 5px;
                    padding-left: 10px;
                }

                QLabel {
                    font-family: Comic Sans MS;
                    letter-spacing: 2px;
                    border-radius: 10px;
                }
            """)

            # WIDGETS
            self.name_lbl = Widgets.QLabel(name)
            self.name_lbl.setObjectName("name_lbl")
            self.name_lbl.setStyleSheet("""
                QLabel#name_lbl {
                    font-size: 25px;
                    font-weight: bold;
                }
            """)

            self.present_frame = Widgets.QFrame()
            self.present_frame.setObjectName("present_frame")
            self.present_layout = Widgets.QVBoxLayout(self.present_frame)
            self.present_lbl = Widgets.QLabel("PRESENT:")
            self.present_lbl.setObjectName("present_lbl")
            self.present_checkbox = Widgets.QCheckBox()
            self.present_lbl.setStyleSheet("""
                QLabel#present_lbl {
                    font-size: 15px;
                    font-weight: bold;
                }
            """)

            self.absent_frame = Widgets.QFrame()
            self.absent_frame.setObjectName("absent_frame")
            self.absent_layout = Widgets.QVBoxLayout(self.absent_frame)
            self.absent_lbl = Widgets.QLabel("ABSENT:")
            self.absent_lbl.setObjectName("absent_lbl")
            self.absent_checkbox = Widgets.QCheckBox()
            self.absent_frame.setStyleSheet("""
                QLabel#absent_lbl {
                    font-size: 15px;
                    font-weight: bold; 
                }
            """)

            self.delete_frame = Widgets.QFrame()
            self.delete_frame.setObjectName("delete_frame")
            self.delete_layout = Widgets.QVBoxLayout(self.delete_frame)
            self.delete_lbl = Widgets.QLabel("DELETE:")
            self.delete_lbl.setObjectName("delete_lbl")
            self.delete_btn = Widgets.QPushButton()
            self.delete_btn.setObjectName("delete_btn")
            self.delete_btn.setFixedSize(Core.QSize(50, 30))
            self.delete_btn.clicked.connect(self.Remove_Person)
            self.delete_btn.setIcon(Gui.QIcon("trash-bin-closed-svgrepo-com.svg"))

            self.delete_frame.setStyleSheet("""
                QPushButton#delete_btn {
                    margin-bottom: 5px;
                    background: #ff1e1e;
                }
                QLabel#delete_lbl {
                    font-size: 15px;
                    font-weight: bold; 
                }
            """)

            self.present_layout.addWidget(self.present_lbl, alignment=Core.Qt.AlignmentFlag.AlignCenter)
            self.present_layout.addWidget(self.present_checkbox, alignment=Core.Qt.AlignmentFlag.AlignCenter)

            self.absent_layout.addWidget(self.absent_lbl, alignment=Core.Qt.AlignmentFlag.AlignCenter)
            self.absent_layout.addWidget(self.absent_checkbox, alignment=Core.Qt.AlignmentFlag.AlignCenter)

            self.delete_layout.addWidget(self.delete_lbl, alignment=Core.Qt.AlignmentFlag.AlignHCenter)
            self.delete_layout.addWidget(self.delete_btn, alignment=Core.Qt.AlignmentFlag.AlignHCenter)
            # ------------------------------------------------------------------------------------------------------

            self.members_layout.addWidget(self.name_lbl)
            self.members_layout.addWidget(self.present_frame)
            self.members_layout.addWidget(self.absent_frame)
            self.members_layout.addWidget(self.delete_frame)

        def Remove_Person(self):
            self.close()

    def Add_Person(self):
        people_to_add: list[str] = self.add_person.displayText().split(", ")

        for person in people_to_add:
            if people_to_add and person.isalpha():
                self.main_frame_layout.addWidget(self.Members_box(person))
                self.add_person.setText("")

    def Complete(self):
        member_boxes = self.main_frame.findChildren(self.Members_box)
        for box in member_boxes:
            if box.present_checkbox.isChecked():
                self.member_list.append(box.name_lbl.text())

        return self.member_list

