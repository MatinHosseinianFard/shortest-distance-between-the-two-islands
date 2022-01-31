from PyQt5 import QtCore, QtGui, QtWidgets

import Land


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 607)
        MainWindow.setStyleSheet("background-color: #D6E6F2;")
        MainWindow.setWindowIcon(QtGui.QIcon('island.png'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.showButton = QtWidgets.QPushButton(self.centralwidget)
        self.showButton.setGeometry(QtCore.QRect(270, 510, 131, 41))
        self.showButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.showButton.setStyleSheet("QPushButton{\n"
                                      "                                        background-color: #536162; \n"
                                      "                                        border: none;\n"
                                      "                                        color: white;\n"
                                      "                                        text-align: center;\n"
                                      "                                        text-decoration: none;\n"
                                      "                                        display: inline-block;\n"
                                      "                                        font-size: 17px;\n"
                                      "                                        border-radius: 8px;\n"
                                      "                                        color: #F3F4ED;\n"
                                      "                                        }\n"
                                      "                                        QshowButton::hover{\n"
                                      "                                         \n"
                                      "                                            background-color : #464F41;\n"
                                      "                                        }")
        self.showButton.setObjectName("showButton")
        self.showButton.clicked.connect(self.get_input)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(120, 30, 431, 451))
        self.textEdit.setStyleSheet("border-radius: 10px;\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "padding:5px;")
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Island"))
        self.showButton.setText(_translate("MainWindow", "Show"))
        self.textEdit.setHtml(_translate("MainWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
                                         "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("MainWindow", ". . ."))

    def get_input(self):
        value = self.textEdit.toPlainText().split()
        matrix = []
        row_number, column_number = map(int, value[:2])
        s = 2
        e = 2 + column_number
        for i in range(row_number):
            matrix.append(list(map(int, value[s:e])))
            s = e
            e += column_number

        MainWindow.hide()
        self.land = QtWidgets.QWidget()
        self.ui = Land.Ui_Form(matrix)
        self.ui.setupUi(self.land)
        self.land.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
