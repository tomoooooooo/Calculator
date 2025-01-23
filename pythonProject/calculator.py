from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(204, 293)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Display setup
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 0, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight | QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lineEdit.setObjectName("lineEdit")

        # Button setup
        font.setPointSize(20)
        self.number7 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number7.setGeometry(QtCore.QRect(0, 50, 51, 51))
        self.number7.setFont(font)
        self.number7.setObjectName("number7")

        self.number8 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number8.setGeometry(QtCore.QRect(50, 50, 51, 51))
        self.number8.setFont(font)
        self.number8.setObjectName("number8")

        self.number9 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number9.setGeometry(QtCore.QRect(100, 50, 51, 51))
        self.number9.setFont(font)
        self.number9.setObjectName("number9")

        self.Sum = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Sum.setGeometry(QtCore.QRect(150, 50, 51, 51))
        self.Sum.setFont(font)
        self.Sum.setObjectName("Sum")

        self.number4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number4.setGeometry(QtCore.QRect(0, 100, 51, 51))
        self.number4.setFont(font)
        self.number4.setObjectName("number4")

        self.number5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number5.setGeometry(QtCore.QRect(50, 100, 51, 51))
        self.number5.setFont(font)
        self.number5.setObjectName("number5")

        self.number6 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number6.setGeometry(QtCore.QRect(100, 100, 51, 51))
        self.number6.setFont(font)
        self.number6.setObjectName("number6")

        self.Dif = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Dif.setGeometry(QtCore.QRect(150, 100, 51, 51))
        self.Dif.setFont(font)
        self.Dif.setObjectName("Dif")

        self.number1 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number1.setGeometry(QtCore.QRect(0, 150, 51, 51))
        self.number1.setFont(font)
        self.number1.setObjectName("number1")

        self.number2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number2.setGeometry(QtCore.QRect(50, 150, 51, 51))
        self.number2.setFont(font)
        self.number2.setObjectName("number2")

        self.number3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number3.setGeometry(QtCore.QRect(100, 150, 51, 51))
        self.number3.setFont(font)
        self.number3.setObjectName("number3")

        self.Multip = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Multip.setGeometry(QtCore.QRect(150, 150, 51, 51))
        self.Multip.setFont(font)
        self.Multip.setObjectName("Multip")

        self.delete_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.delete_button.setGeometry(QtCore.QRect(0, 200, 51, 51))
        font.setPointSize(15)
        font.setBold(True)
        self.delete_button.setFont(font)
        self.delete_button.setObjectName("delete_button")

        font.setPointSize(20)
        self.number0 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.number0.setGeometry(QtCore.QRect(50, 200, 51, 51))
        self.number0.setFont(font)
        self.number0.setObjectName("number0")

        self.equal_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.equal_button.setGeometry(QtCore.QRect(100, 200, 51, 51))
        self.equal_button.setFont(font)
        self.equal_button.setObjectName("equal_button")

        self.Devide = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Devide.setGeometry(QtCore.QRect(150, 200, 51, 51))
        self.Devide.setFont(font)
        self.Devide.setObjectName("Devide")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 204, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Connect buttons to their respective functions
        self.number0.clicked.connect(lambda: self.append_to_lineEdit("0"))
        self.number1.clicked.connect(lambda: self.append_to_lineEdit("1"))
        self.number2.clicked.connect(lambda: self.append_to_lineEdit("2"))
        self.number3.clicked.connect(lambda: self.append_to_lineEdit("3"))
        self.number4.clicked.connect(lambda: self.append_to_lineEdit("4"))
        self.number5.clicked.connect(lambda: self.append_to_lineEdit("5"))
        self.number6.clicked.connect(lambda: self.append_to_lineEdit("6"))
        self.number7.clicked.connect(lambda: self.append_to_lineEdit("7"))
        self.number8.clicked.connect(lambda: self.append_to_lineEdit("8"))
        self.number9.clicked.connect(lambda: self.append_to_lineEdit("9"))
        self.Sum.clicked.connect(lambda: self.append_to_lineEdit("+"))
        self.Dif.clicked.connect(lambda: self.append_to_lineEdit("-"))
        self.Multip.clicked.connect(lambda: self.append_to_lineEdit("*"))
        self.Devide.clicked.connect(lambda: self.append_to_lineEdit("/"))
        self.delete_button.clicked.connect(self.delete_last_character)
        self.equal_button.clicked.connect(self.calculate_result)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculator"))
        self.number7.setText(_translate("MainWindow", "7"))
        self.number8.setText(_translate("MainWindow", "8"))
        self.number9.setText(_translate("MainWindow", "9"))
        self.Sum.setText(_translate("MainWindow", "+"))
        self.number4.setText(_translate("MainWindow", "4"))
        self.number5.setText(_translate("MainWindow", "5"))
        self.number6.setText(_translate("MainWindow", "6"))
        self.Dif.setText(_translate("MainWindow", "-"))
        self.number1.setText(_translate("MainWindow", "1"))
        self.number2.setText(_translate("MainWindow", "2"))
        self.number3.setText(_translate("MainWindow", "3"))
        self.Multip.setText(_translate("MainWindow", "*"))
        self.delete_button.setText(_translate("MainWindow", "DEL"))
        self.number0.setText(_translate("MainWindow", "0"))
        self.equal_button.setText(_translate("MainWindow", "="))
        self.Devide.setText(_translate("MainWindow", "/"))

    def append_to_lineEdit(self, text):
        current_text = self.lineEdit.text()
        self.lineEdit.setText(current_text + text)

    def delete_last_character(self):
        current_text = self.lineEdit.text()
        if current_text:
            self.lineEdit.setText(current_text[:-1])

    def calculate_result(self):
        expression = self.lineEdit.text()
        try:
            result = eval(expression)
            self.lineEdit.setText(str(result))
        except Exception:
            self.lineEdit.setText("Error")


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
