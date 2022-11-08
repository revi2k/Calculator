# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CalculatorInterface.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(180, 30, 431, 101))
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        font = QtGui.QFont()
        font.setPointSize(24)
        self.lineEdit.setFont(font)

        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(180, 180, 434, 342))
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Number7 = QtWidgets.QPushButton(self.widget)
        self.Number7.setMinimumSize(QtCore.QSize(80, 80))
        self.Number7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number7.setFont(font)
        self.Number7.setObjectName("Number7")
        self.gridLayout.addWidget(self.Number7, 0, 0, 1, 1)
        self.Number8 = QtWidgets.QPushButton(self.widget)
        self.Number8.setMinimumSize(QtCore.QSize(80, 80))
        self.Number8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number8.setFont(font)
        self.Number8.setObjectName("Number8")
        self.gridLayout.addWidget(self.Number8, 0, 1, 1, 1)
        self.Number9 = QtWidgets.QPushButton(self.widget)
        self.Number9.setMinimumSize(QtCore.QSize(80, 80))
        self.Number9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number9.setFont(font)
        self.Number9.setObjectName("Number9")
        self.gridLayout.addWidget(self.Number9, 0, 2, 1, 1)
        self.Number4 = QtWidgets.QPushButton(self.widget)
        self.Number4.setMinimumSize(QtCore.QSize(80, 80))
        self.Number4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number4.setFont(font)
        self.Number4.setObjectName("Number4")
        self.gridLayout.addWidget(self.Number4, 1, 0, 1, 1)
        self.Number5 = QtWidgets.QPushButton(self.widget)
        self.Number5.setMinimumSize(QtCore.QSize(80, 80))
        self.Number5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number5.setFont(font)
        self.Number5.setObjectName("Number5")
        self.gridLayout.addWidget(self.Number5, 1, 1, 1, 1)
        self.Number6 = QtWidgets.QPushButton(self.widget)
        self.Number6.setMinimumSize(QtCore.QSize(80, 80))
        self.Number6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number6.setFont(font)
        self.Number6.setObjectName("Number6")
        self.gridLayout.addWidget(self.Number6, 1, 2, 1, 1)
        self.Number1 = QtWidgets.QPushButton(self.widget)
        self.Number1.setMinimumSize(QtCore.QSize(80, 80))
        self.Number1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number1.setFont(font)
        self.Number1.setObjectName("Number1")
        self.gridLayout.addWidget(self.Number1, 2, 0, 1, 1)
        self.Number2 = QtWidgets.QPushButton(self.widget)
        self.Number2.setMinimumSize(QtCore.QSize(80, 80))
        self.Number2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number2.setFont(font)
        self.Number2.setObjectName("Number2")
        self.gridLayout.addWidget(self.Number2, 2, 1, 1, 1)
        self.Number3 = QtWidgets.QPushButton(self.widget)
        self.Number3.setMinimumSize(QtCore.QSize(80, 80))
        self.Number3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number3.setFont(font)
        self.Number3.setObjectName("Number3")
        self.gridLayout.addWidget(self.Number3, 2, 2, 1, 1)
        self.Number0 = QtWidgets.QPushButton(self.widget)
        self.Number0.setMinimumSize(QtCore.QSize(80, 80))
        self.Number0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Number0.setFont(font)
        self.Number0.setObjectName("Number0")
        self.gridLayout.addWidget(self.Number0, 3, 0, 1, 1)
        self.Dot = QtWidgets.QPushButton(self.widget)
        self.Dot.setMinimumSize(QtCore.QSize(80, 80))
        self.Dot.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Dot.setFont(font)
        self.Dot.setObjectName("Dot")
        self.gridLayout.addWidget(self.Dot, 3, 1, 1, 1)
        self.Clear = QtWidgets.QPushButton(self.widget)
        self.Clear.setMinimumSize(QtCore.QSize(80, 80))
        self.Clear.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Clear.setFont(font)
        self.Clear.setObjectName("Dot")
        self.gridLayout.addWidget(self.Clear, 3, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.CloseApp = QtWidgets.QPushButton(self.widget)
        self.CloseApp.setMinimumSize(QtCore.QSize(170, 80))
        self.CloseApp.setMaximumSize(QtCore.QSize(170, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.CloseApp.setFont(font)
        self.CloseApp.setAutoFillBackground(False)
        self.CloseApp.setObjectName("CloseApp")
        self.gridLayout_2.addWidget(self.CloseApp, 0, 0, 1, 2)
        self.Operation1 = QtWidgets.QPushButton(self.widget)
        self.Operation1.setMinimumSize(QtCore.QSize(80, 80))
        self.Operation1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Operation1.setFont(font)
        self.Operation1.setObjectName("Operation1")
        self.gridLayout_2.addWidget(self.Operation1, 1, 0, 1, 1)
        self.Operation2 = QtWidgets.QPushButton(self.widget)
        self.Operation2.setMinimumSize(QtCore.QSize(80, 80))
        self.Operation2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Operation2.setFont(font)
        self.Operation2.setObjectName("Operation2")
        self.gridLayout_2.addWidget(self.Operation2, 1, 1, 1, 1)
        self.Operation3 = QtWidgets.QPushButton(self.widget)
        self.Operation3.setMinimumSize(QtCore.QSize(80, 80))
        self.Operation3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Operation3.setFont(font)
        self.Operation3.setObjectName("Operation3")
        self.gridLayout_2.addWidget(self.Operation3, 2, 0, 1, 1)
        self.Operation4 = QtWidgets.QPushButton(self.widget)
        self.Operation4.setMinimumSize(QtCore.QSize(80, 80))
        self.Operation4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Operation4.setFont(font)
        self.Operation4.setObjectName("Operation4")
        self.gridLayout_2.addWidget(self.Operation4, 2, 1, 1, 1)
        self.Operation5 = QtWidgets.QPushButton(self.widget)
        self.Operation5.setMinimumSize(QtCore.QSize(80, 80))
        self.Operation5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Operation5.setFont(font)
        self.Operation5.setObjectName("Operation5")
        self.gridLayout_2.addWidget(self.Operation5, 3, 0, 1, 1)
        self.Operation6 = QtWidgets.QPushButton(self.widget)
        self.Operation6.setMinimumSize(QtCore.QSize(80, 80))
        self.Operation6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Calibri Light")
        font.setPointSize(20)
        self.Operation6.setFont(font)
        self.Operation6.setObjectName("Operation6")
        self.gridLayout_2.addWidget(self.Operation6, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        #OPERATIONS: 1:X,2:/,3:-,4:+,5:%,6:=
        self.number_in_queue2 = ""
        self.current_result = 0.0
        self.last_signal = None

        def error(errorType): # error function, popup window with error type
                msg = QMessageBox()
                msg.setWindowTitle("Error")
                msg.setText(errorType)
                x = msg.exec_()
                return x

        def last_signal(): # last singal function, necessary to identify last operation
            if self.last_signal == 'Add':
                self.last_signal = None
                add()
            elif self.last_signal == 'Sub':
                self.last_signal = None
                sub()
            elif self.last_signal == 'Mul':
                self.last_signal = None
                mult()
            elif self.last_signal == 'Div':
                self.last_signal = None
                divi()

        def add(): # add function
            last_signal()
            if self.number_in_queue2 == "":
                self.lineEdit.setText(str(self.current_result))
                self.number_in_queue2 = ""
                self.last_signal = 'Add'
            else:
                self.current_result += float(self.number_in_queue2)
                self.lineEdit.setText(str(self.current_result))
                self.number_in_queue2 = ""
                self.last_signal = 'Add' 

        def sub(): # subtract function
            last_signal()
            if self.number_in_queue2 == "":
                self.lineEdit.setText(str(self.current_result))
                self.number_in_queue2 = ""
                self.last_signal = 'Sub'
            else:
                self.current_result -= float(self.number_in_queue2)
                self.lineEdit.setText(str(self.current_result))
                self.number_in_queue2 = ""
                self.last_signal = 'Sub'
        def mult(): # multiple function
            last_signal()
            if self.number_in_queue2 == "":
                self.lineEdit.setText(str(self.current_result))
                self.number_in_queue2 = ""
                self.last_signal = 'Mul'
            else:
                if self.current_result > 0:
                    self.current_result = self.current_result * float(self.number_in_queue2)
                    self.lineEdit.setText(str(self.current_result))
                    self.number_in_queue2 = ""
                    self.last_signal = 'Mul'
                else:
                    self.current_result = float(self.number_in_queue2)
                    self.number_in_queue2 = ""
                    self.last_signal = 'Mul'
        def divi(): # divide function
            try:
                last_signal()
                if self.number_in_queue2 == "":
                    self.lineEdit.setText(str(self.current_result))
                    self.number_in_queue2 = ""
                    self.last_signal = 'Div'
                else:
                    if self.current_result > 0:
                        self.current_result = self.current_result / float(self.number_in_queue2)
                        self.lineEdit.setText(str(self.current_result))
                        self.number_in_queue2 = ""
                        self.last_signal = 'Div'
                    else:
                        self.current_result = float(self.number_in_queue2)
                        self.number_in_queue2 = ""
                        self.last_signal = 'Div'
            except ZeroDivisionError:
                error("You can't divide by 0!")
                clear()

        def return_number0():
            self.number_in_queue2 += "0"
        def return_number1():
            self.number_in_queue2 += "1"
        def return_number2():
            self.number_in_queue2 += "2"
        def return_number3():
            self.number_in_queue2 += "3"
        def return_number4():
            self.number_in_queue2 += "4"
        def return_number5():
            self.number_in_queue2 += "5"
        def return_number6():
            self.number_in_queue2 += "6"
        def return_number7():
            self.number_in_queue2 += "7"
        def return_number8():
            self.number_in_queue2 += "8"
        def return_number9():
            self.number_in_queue2 += "9"
        def update():
            self.lineEdit.setText(self.number_in_queue2)
        def result():
            last_signal()
            self.lineEdit.setText(str(self.current_result))
        def clear():
            self.current_result = 0
            self.number_in_queue2 = ""
            self.lineEdit.setText(None)



        #BUTTONS ACTIONS
        self.CloseApp.clicked.connect(exit)

        self.Operation1.clicked.connect(mult)
        self.Operation1.clicked.connect(last_signal)

        self.Operation2.clicked.connect(divi)
        self.Operation2.clicked.connect(last_signal)

        self.Operation3.clicked.connect(sub)
        self.Operation3.clicked.connect(last_signal)

        self.Operation4.clicked.connect(add)
        self.Operation4.clicked.connect(last_signal)

        self.Operation6.clicked.connect(result)
        self.Clear.clicked.connect(clear)

        self.Number0.clicked.connect(return_number0)
        self.Number0.clicked.connect(update)

        self.Number1.clicked.connect(return_number1)
        self.Number1.clicked.connect(update)

        self.Number2.clicked.connect(return_number2)
        self.Number2.clicked.connect(update)

        self.Number3.clicked.connect(return_number3)
        self.Number3.clicked.connect(update)

        self.Number4.clicked.connect(return_number4)
        self.Number4.clicked.connect(update)

        self.Number5.clicked.connect(return_number5)
        self.Number5.clicked.connect(update)

        self.Number6.clicked.connect(return_number6)
        self.Number6.clicked.connect(update)

        self.Number7.clicked.connect(return_number7)
        self.Number7.clicked.connect(update)

        self.Number8.clicked.connect(return_number8)
        self.Number8.clicked.connect(update)

        self.Number9.clicked.connect(return_number9)    
        self.Number9.clicked.connect(update)   



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Number7.setText(_translate("MainWindow", "7"))
        self.Number8.setText(_translate("MainWindow", "8"))
        self.Number9.setText(_translate("MainWindow", "9"))
        self.Number4.setText(_translate("MainWindow", "4"))
        self.Number5.setText(_translate("MainWindow", "5"))
        self.Number6.setText(_translate("MainWindow", "6"))
        self.Number1.setText(_translate("MainWindow", "1"))
        self.Number2.setText(_translate("MainWindow", "2"))
        self.Number3.setText(_translate("MainWindow", "3"))
        self.Number0.setText(_translate("MainWindow", "0"))
        self.Dot.setText(_translate("MainWindow", "."))
        self.Clear.setText(_translate("MainWindow", "CLEAR"))
        self.CloseApp.setText(_translate("MainWindow", "OFF"))
        self.Operation1.setText(_translate("MainWindow", "X"))
        self.Operation2.setText(_translate("MainWindow", "/"))
        self.Operation3.setText(_translate("MainWindow", "-"))
        self.Operation4.setText(_translate("MainWindow", "+"))
        self.Operation5.setText(_translate("MainWindow", ""))
        self.Operation6.setText(_translate("MainWindow", "="))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    app.setStyle('Fusion')
    MainWindow.show()
    sys.exit(app.exec_())
