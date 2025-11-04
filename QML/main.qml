import QtQuick 2.15
import QtQuick.Controls.Basic 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15

ApplicationWindow {
    id: root
    visible: true
    width: Screen.width * 0.6
    height: Screen.height * 0.75
    x: (Screen.width - width) / 2
    y: (Screen.height - height) / 2
    title: "PySide6 + QML"

    // -----------------------
    // Start Button
    // -----------------------
    Button {
        id: start_button
        objectName: "start_button"
        anchors.centerIn: parent

        background: Rectangle {
            implicitWidth: 250
            implicitHeight: 150

            color: start_button.down ? "#DE0182E5" :
                    start_button.hovered ? "#B8007EE6" : "#0089FF"
            border.color: "#0059FF"
            border.width: 4
            radius: 10

            Behavior on color {
                ColorAnimation { duration: 500; easing.type: Easing.InOutQuad }
            }
        }

        contentItem: Item {
            anchors.fill: parent
            Text {
                anchors.centerIn: parent
                text: "Start Game"
                font.family: "Comic Sans MS"
                font.pointSize: 25
                font.bold: true
                color: "#0F0E0E"
            }
        }

        onClicked: {
            backend.clear_buttons()
            backend.create_blanks()
            backend.generate_tries()

        }
    }
    
    // -----------------------
    // status_img
    // -----------------------
    Image {
        id: status_img
        objectName: "status_img"
        sourceSize.width: 85 // No matter the size of the .png or jpg, 
        sourceSize.height: 85 // you can adjust with sourceSize.width/height
        anchors.bottom: contentColumn.top
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.bottomMargin: 20
        visible: false

    }

    Column {
        id: contentColumn
        objectName: "contentColumn"
        anchors.centerIn: parent
        spacing: 30  // adds vertical space in between every element
        visible: false 


        // -----------------------
        // blank_lbl
        // -----------------------
        Label {
            id: blank_lbl
            objectName: "blank_lbl"
            text: ""
            font.pointSize: 40
            font.family: "Comic Sans MS"
            font.bold: true
            anchors.horizontalCenter: parent.horizontalCenter

        }

        // -----------------------
        // Input Row - positioned below the label
        // -----------------------
        Row {
            id: contentRow_in_contentColumn
            spacing: 15
            anchors.horizontalCenter: parent.horizontalCenter
            height: 60  // Match the button height

            TextField {
                id: users_answer_TF
                objectName: "users_answer_TF"
                width: 250
                height: 60  // Match the row height
                placeholderText: "Type here ..."
                font.pointSize: 20
                font.family: "Comic Sans MS"
                leftPadding: 15
                verticalAlignment: TextInput.AlignVCenter

                background: Rectangle {
                    color: "white"
                    border.color: "black"
                    border.width: 3
                    radius: 8
                }
                onAccepted: {
                    backend.users_answer_from_TF(text)
                }


            }

            Button { 
                id: enter_btn
                objectName: "enter_btn"
                width: 60
                height: 60

                background: Rectangle {
                    color: enter_btn.down ? "#DE0182E5" :
                            enter_btn.hovered ? "#B8007EE6" : "#0089FF"
                    border.color: "#0059FF"
                    border.width: 4
                    radius: 10

                    Behavior on color {
                        ColorAnimation { duration: 500; easing.type: Easing.InOutQuad }
                    }
                }

                contentItem: Image {
                    source: "./right-arrow.png"
                    sourceSize.width: 35
                    sourceSize.height: 35
                    
                }

                onClicked: backend.users_answer_from_btn()
            }

        }

    }

    // ---------------------------------------------------
    // messages_lbl
    // ---------------------------------------------------
    Label {
        id: messages_lbl
        objectName: "messages_lbl"
        text: ""
        font.pointSize: 18
        font.family: "Comic Sans MS"
        font.bold: true
        anchors.top: contentColumn.bottom
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.topMargin: 20
        visible: false

    }


    // ---------------------------------------------------
    // tries_lbl
    // ---------------------------------------------------
    Label {
        id: tries_lbl 
        objectName: "tries_lbl"
        text: "Tries left: 0"
        font.pointSize: 25
        font.family: "Comic Sans MS"
        font.bold: true
        anchors.left: parent.left
        anchors.bottom: parent.bottom
        anchors.margins: 20
        visible: false

    }

    Timer { // hide_timer
        id: hide_timer
        interval: 3000
        onTriggered: { 
            status_img.visible = false 
            messages_lbl.visible = false 

        }
    }
    // to receive Signal(stuff)
    Connections {
        target: backend

        function onRight_or_wrong(bool, chosen_word) {
            status_img.visible = true

            if ( bool ) {
                status_img.source = "./check.png" 
                blank_lbl.text = chosen_word
                enter_btn.enabled = false

            } else {
                status_img.source = "./wrong.png" 

            }

            hide_timer.restart()
        }

        function onError_popup(bool, message) {
            if ( bool ) {
                messages_lbl.visible = true
                messages_lbl.text = message
            }  

            hide_timer.restart()

        }
    }

}