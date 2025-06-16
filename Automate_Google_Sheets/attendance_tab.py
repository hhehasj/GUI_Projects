import PySide6.QtGui as Gui
import PySide6.QtWidgets as Widgets
import PySide6.QtCore as Core
import database as db


class AttendanceTab(Widgets.QFrame):
    member_list: list[str] = []

    def __init__(self):
        super().__init__()

        self.main_layout = Widgets.QVBoxLayout(self)
        self.scroll_area = Widgets.QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.main_frame = Widgets.QFrame()
        self.scroll_area.setWidget(self.main_frame)
        self.main_frame_layout = Widgets.QVBoxLayout(self.main_frame)

        for member in db.get_members():  # When the GUI starts
            self.main_frame_layout.addWidget(self.Members_box(member))

        self.sub_layout = Widgets.QHBoxLayout()
        self.add_person = Widgets.QLineEdit()
        self.add_person.setObjectName("add_person")
        self.add_person.setMaximumSize(500, 50)

        self.add_person_btn = Widgets.QPushButton("Add Person")
        self.add_person_btn.setObjectName("add_person_btn")
        self.add_person_btn.setMaximumSize(200, 50)
        self.add_person_btn.clicked.connect(self.Add_Person)

        self.SaveToDB_frame = Widgets.QFrame()
        self.SaveToDB_layout = Widgets.QVBoxLayout(self.SaveToDB_frame)
        self.SaveToDB_layout.setContentsMargins(0, 0, 0, 0)
        self.SaveToDB_layout.setSpacing(0)
        self.SaveToDB_lbl = Widgets.QLabel("Save:")
        self.SaveToDB_lbl.setObjectName("SaveToDB_lbl")
        self.SaveToDB_CB = Widgets.QCheckBox("")
        self.SaveToDB_CB.setObjectName("SaveToDB_CB")

        # --------------------------------------------------------------------------------------------------
        self.SaveToDB_layout.addWidget(self.SaveToDB_lbl, alignment=Core.Qt.AlignmentFlag.AlignHCenter)
        self.SaveToDB_layout.addWidget(self.SaveToDB_CB, alignment=Core.Qt.AlignmentFlag.AlignHCenter)
        # --------------------------------------------------------------------------------------------------

        self.complete_btn = Widgets.QPushButton("COMPLETE")
        self.complete_btn.setObjectName("complete_btn")
        self.complete_btn.setMaximumSize(200, 50)
        self.complete_btn.clicked.connect(self.Complete)

        # STYLESHEET of the widgets at the bottom.
        self.setStyleSheet("""
            QPushButton {
                font: 25px Comic Sans MS;
                letter-spacing: 2px;
                background-color: hsl(220, 100%, 70%);
                border: 3px solid black;
                border-radius: 10px;
                padding-left: 10px;
                padding-right: 10px;
            }
            QPushButton:hover {
                background-color: hsl(210, 80%, 50%);    
            }
            QPushButton:pressed {
                background-color: hsl(210, 100%, 40%);
            }
            
            QLineEdit#add_person {
                font: 20px Comic Sans MS;
                border: 2px solid black;
                border-radius: 5px;
                padding-left: 10px;
            }
            
            QCheckBox#SaveToDB_CB::indicator {
                width: 30px; 
                height: 30px; 
            }
            QCheckBox#SaveToDB_CB::indicator:unchecked {
                image: url(icons/squircle3.svg); 
            }
            QCheckBox#SaveToDB_CB::indicator:checked {
                image: url(icons/rounded_checked5.svg); 
            }
            
            QLabel {
                font: 20px Comic Sans MS;
                font-weight: bold;
            }
        """)

        # -------------------------------------------------------------------------------------------
        self.main_layout.addWidget(self.scroll_area, alignment=Core.Qt.AlignmentFlag.AlignTop)
        self.main_layout.addLayout(self.sub_layout)
        self.sub_layout.addWidget(self.add_person)
        self.sub_layout.addWidget(self.SaveToDB_frame)
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
                    font: 15px Comic Sans MS;
                    font-weight: bold;
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
                }
            """)

            self.present_frame = Widgets.QFrame()
            self.present_layout = Widgets.QVBoxLayout(self.present_frame)
            self.present_lbl = Widgets.QLabel("PRESENT:")
            self.present_checkbox = Widgets.QCheckBox(" ")

            self.absent_frame = Widgets.QFrame()
            self.absent_layout = Widgets.QVBoxLayout(self.absent_frame)
            self.absent_lbl = Widgets.QLabel("ABSENT:")
            self.absent_checkbox = Widgets.QCheckBox(" ")

            self.delete_frame = Widgets.QFrame()
            self.delete_layout = Widgets.QVBoxLayout(self.delete_frame)
            self.delete_lbl = Widgets.QLabel("DELETE:")
            self.delete_btn = Widgets.QPushButton()
            self.delete_btn.setObjectName("delete_btn")
            self.delete_btn.setFixedSize(Core.QSize(50, 30))
            self.delete_btn.clicked.connect(self.Remove_Person)
            self.delete_btn.setIcon(Gui.QIcon("icons/trash-bin-closed-svgrepo-com.svg"))

            self.delete_frame.setStyleSheet("""
                QPushButton#delete_btn {
                    margin-bottom: 5px;
                    background-color: hsl(355, 100%, 50%);
                }
                QPushButton#delete_btn:hover {
                    background-color: hsl(355, 100%, 45%);
                }
                QPushButton#delete_btn:pressed {
                    background-color: hsl(355, 100%, 40%);
                }
            """)

            # --------------------------------------------------------------------------------------------------
            self.present_layout.addWidget(self.present_lbl, alignment=Core.Qt.AlignmentFlag.AlignCenter)
            self.present_layout.addWidget(self.present_checkbox, alignment=Core.Qt.AlignmentFlag.AlignCenter)

            self.absent_layout.addWidget(self.absent_lbl, alignment=Core.Qt.AlignmentFlag.AlignCenter)
            self.absent_layout.addWidget(self.absent_checkbox, alignment=Core.Qt.AlignmentFlag.AlignCenter)

            self.delete_layout.addWidget(self.delete_lbl, alignment=Core.Qt.AlignmentFlag.AlignHCenter)
            self.delete_layout.addWidget(self.delete_btn, alignment=Core.Qt.AlignmentFlag.AlignHCenter)
            # --------------------------------------------------------------------------------------------------

            self.members_layout.addWidget(self.name_lbl)
            self.members_layout.addWidget(self.present_frame)
            self.members_layout.addWidget(self.absent_frame)
            self.members_layout.addWidget(self.delete_frame)

        def Remove_Person(self):
            db.remove(self.name_lbl.text())
            self.close()

    def Save(self):
        return self.SaveToDB_CB.isChecked()

    def Add_Person(self):
        people_to_add: list[str] = self.add_person.displayText().split(", ")
        to_save: bool = self.Save()

        for person in people_to_add:
            if people_to_add and person.isalpha() and to_save is False:
                self.main_frame_layout.addWidget(self.Members_box(person))
                self.add_person.setText("")

            if people_to_add and person.isalpha() and to_save:
                self.main_frame_layout.addWidget(self.Members_box(person))
                db.save(person)
                self.add_person.setText("")

    def Complete(self):
        member_boxes = self.main_frame.findChildren(self.Members_box)
        for box in member_boxes:
            if box.present_checkbox.isChecked():
                self.member_list.append(box.name_lbl.text())

        return self.member_list

