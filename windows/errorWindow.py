from PyQt6 import QtWidgets, QtCore, QtGui


class UiErrorWindow(object): # Класс, задающий параметры окна "Сообщить об ошибке"
    def _setup_ui_(self, error_window):
        error_window.setObjectName("error_window")
        error_window.resize(745, 233)
        self.central_widget = QtWidgets.QWidget(parent=error_window)
        self.central_widget.setObjectName("central_widget")
        self.label_icon = QtWidgets.QLabel(parent=self.central_widget)
        self.label_icon.setGeometry(QtCore.QRect(10, 30, 181, 141))
        self.label_icon.setText("")
        self.label_icon.setPixmap(QtGui.QPixmap("resources/splash_screen_pic.png"))
        self.label_icon.setObjectName("label_icon")
        self.groupBox = QtWidgets.QGroupBox(parent=self.central_widget)
        self.groupBox.setGeometry(QtCore.QRect(210, 30, 491, 141))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_info = QtWidgets.QLabel(parent=self.groupBox)
        self.label_info.setGeometry(QtCore.QRect(10, 10, 471, 111))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setObjectName("label_info")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.central_widget)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 190, 321, 21))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_ver = QtWidgets.QLabel(parent=self.groupBox_2)
        self.label_ver.setGeometry(QtCore.QRect(120, 0, 101, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_ver.setFont(font)
        self.label_ver.setObjectName("label_ver")
        self.exitButton = QtWidgets.QPushButton(parent=self.central_widget)
        self.exitButton.setGeometry(QtCore.QRect(580, 190, 75, 23))
        self.exitButton.setObjectName("exitButton")
        error_window.setCentralWidget(self.central_widget)

        self._retranslate_ui_(error_window)
        QtCore.QMetaObject.connectSlotsByName(error_window)
        self.exitButton.clicked.connect(error_window.close)

    def _retranslate_ui_(self, error_window):
        _translate = QtCore.QCoreApplication.translate
        error_window.setWindowTitle(_translate("error_window", "Сообщить об ошибке"))
        self.label_info.setText(_translate("error_window",
                                        "<html><head/><body><p>Если программа работает некорректно, обнаружена ошибка в формулах </p><p>или есть предложение по функционалу программы, обратитесь по следующей</p><p>электронной почте: </p><p></p></body></html>"))
        self.label_ver.setText(_translate("error_window", "Версия 1.0.0.2023"))
        self.exitButton.setText(_translate("error_window", "Выход"))