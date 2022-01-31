from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QBrush, QPen, QPainter
import Main


class Ui_Form(object):
    def __init__(self, matrix):
        self.matrix = matrix

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(667, 606)
        Form.setStyleSheet("background-color: #5cbcfc;")
        Form.setWindowIcon(QtGui.QIcon('island.png'))
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(24, 20, 621, 391))
        self.label.setText("")
        self.label.setObjectName("label")
        canvas = QtGui.QPixmap(621, 391)
        canvas.fill(QtGui.QColor('#5cbcfc'))
        self.label.setPixmap(canvas)

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(270, 440, 151, 31))
        self.label_2.setText("")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("                                        background-color: #e3f2fd; \n"
                                   "                                        border-radius: 10px;\n"
                                   "                                        font-size: 15px\n;"
                                   "                                       ")

        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(270, 490, 151, 31))
        self.label_3.setText("")
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet("                                        background-color: #e3f2fd; \n"
                                   "                                        border-radius: 10px;\n"
                                   "                                        font-size: 15px\n;"
                                   "                                       ")

        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(270, 540, 151, 31))
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_4.setStyleSheet("                                        background-color: #e3f2fd; \n"
                                   "                                        border-radius: 10px;\n"
                                   "                                        font-size: 15px\n;"
                                   "                                       ")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.show_land()

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Land"))

    def show_land(self):
        painter = QtGui.QPainter(self.label.pixmap())
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QBrush(Qt.black, Qt.SolidPattern))
        painter.setPen(QPen(Qt.black, 3, Qt.SolidLine))

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                if self.matrix[i][j] == 1:
                    x = (j + 9) * 15
                    y = (i + 2) * 15
                    width, height = 5, 5
                    painter.drawEllipse(x, y, width, height)

                # else:
                #     painter.drawPoint(x, y)

        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        resault = Main.solve(self.matrix)
        painter.drawLine((resault[0][1] + 9) * 15, (resault[0][0] + 2) * 15, (resault[1][1] + 9) * 15,
                         (resault[1][0] + 2) * 15)
        painter.end()

        self.label_2.setText(f"az deraye : {resault[0]}")
        self.label_3.setText(f"ta deraye : {resault[1]}")
        self.label_4.setText(f"fasele : {resault[2]}")
