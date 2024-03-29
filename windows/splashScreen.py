from PyQt6 import QtCore, QtGui, QtWidgets


class UiSplashScreen(object): # Класс, задающий параметры Splash Screen`а
    def _setup_ui_(self, splash_screen):
        splash_screen.setObjectName("splash_screen")
        splash_screen.resize(624, 392)
        splash_screen.setMaximumSize(624, 392)
        splash_screen.setMinimumSize(624, 392)
        self.central_widget = QtWidgets.QWidget(parent=splash_screen)
        self.central_widget.setObjectName("central_widget")
        self.label_univ = QtWidgets.QLabel(parent=self.central_widget)
        self.label_univ.setGeometry(QtCore.QRect(140, 0, 391, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_univ.setFont(font)
        self.label_univ.setObjectName("label_univ")
        self.label_fac = QtWidgets.QLabel(parent=self.central_widget)
        self.label_fac.setGeometry(QtCore.QRect(120, 30, 421, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_fac.setFont(font)
        self.label_fac.setObjectName("label_fac")
        self.label_caf = QtWidgets.QLabel(parent=self.central_widget)
        self.label_caf.setGeometry(QtCore.QRect(60, 50, 541, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_caf.setFont(font)
        self.label_caf.setObjectName("label_caf")
        self.label_prog = QtWidgets.QLabel(parent=self.central_widget)
        self.label_prog.setGeometry(QtCore.QRect(230, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_prog.setFont(font)
        self.label_prog.setObjectName("label_prog")
        self.label_disc = QtWidgets.QLabel(parent=self.central_widget)
        self.label_disc.setGeometry(QtCore.QRect(150, 130, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_disc.setFont(font)
        self.label_disc.setObjectName("label_disc")
        self.label_lang = QtWidgets.QLabel(parent=self.central_widget)
        self.label_lang.setGeometry(QtCore.QRect(270, 130, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        self.label_lang.setFont(font)
        self.label_lang.setObjectName("label_lang")
        self.label_func = QtWidgets.QLabel(parent=self.central_widget)
        self.label_func.setGeometry(QtCore.QRect(160, 150, 291, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_func.setFont(font)
        self.label_func.setObjectName("label_func")
        self.label_stud = QtWidgets.QLabel(parent=self.central_widget)
        self.label_stud.setGeometry(QtCore.QRect(300, 200, 271, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stud.setFont(font)
        self.label_stud.setObjectName("label_stud")
        self.label_name = QtWidgets.QLabel(parent=self.central_widget)
        self.label_name.setGeometry(QtCore.QRect(300, 220, 191, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setObjectName("label_name")
        self.label_lect = QtWidgets.QLabel(parent=self.central_widget)
        self.label_lect.setGeometry(QtCore.QRect(300, 250, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_lect.setFont(font)
        self.label_lect.setObjectName("label_lect")
        self.label_lect_name = QtWidgets.QLabel(parent=self.central_widget)
        self.label_lect_name.setGeometry(QtCore.QRect(300, 270, 241, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_lect_name.setFont(font)
        self.label_lect_name.setObjectName("label_lect_name")
        self.label_minsk = QtWidgets.QLabel(parent=self.central_widget)
        self.label_minsk.setGeometry(QtCore.QRect(260, 310, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_minsk.setFont(font)
        self.label_minsk.setObjectName("label_minsk")
        self.button_next = QtWidgets.QPushButton(parent=self.central_widget)
        self.button_next.setGeometry(QtCore.QRect(320, 340, 291, 41))
        self.button_next.setObjectName("button_next")
        self.button_exit = QtWidgets.QPushButton(parent=self.central_widget)
        self.button_exit.setGeometry(QtCore.QRect(10, 340, 291, 41))
        self.button_exit.setObjectName("button_exit")
        self.label_image = QtWidgets.QLabel(parent=self.central_widget)
        self.label_image.setGeometry(QtCore.QRect(60, 180, 191, 141))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_image.setFont(font)
        self.label_image.setText("")
        self.label_image.setPixmap(QtGui.QPixmap("resources/splash_screen_pic.png"))
        self.label_image.setObjectName("label_image")
        splash_screen.setCentralWidget(self.central_widget)

        self._retranslate_ui_(splash_screen)
        self.button_exit.clicked.connect(splash_screen.close)
        QtCore.QMetaObject.connectSlotsByName(splash_screen)

    def _retranslate_ui_(self, splash_screen):
        _translate = QtCore.QCoreApplication.translate
        splash_screen.setWindowTitle(_translate("splash_screen", "Построение графиков функций"))
        self.label_univ.setText(_translate("splash_screen", "Белорусский национальный технический университет"))
        self.label_fac.setText(_translate("splash_screen", "Факультет информационных технологий и робототехники"))
        self.label_caf.setText(
            _translate("splash_screen", "Кафедра программного обеспечения информационных систем и технологий"))
        self.label_prog.setText(_translate("splash_screen", "Курсовой проект"))
        self.label_disc.setText(_translate("splash_screen", "По дисциплине "))
        self.label_lang.setText(_translate("splash_screen", "Языки программирования"))
        self.label_func.setText(_translate("splash_screen", "Построение графиков функций"))
        self.label_stud.setText(_translate("splash_screen", "Выполнил: Студент группы "))
        self.label_name.setText(_translate("splash_screen", ""))
        self.label_lect.setText(
            _translate("splash_screen", "<html><head/><body><p>Преподователь: к.ф-м.н, доц.</p></body></html>"))
        self.label_lect_name.setText(
            _translate("splash_screen", "<html><head/><body><p></p></body></html>"))
        self.label_minsk.setText(_translate("splash_screen", "Минск, 2023"))
        self.button_next.setText(_translate("splash_screen", "Далее"))
        self.button_exit.setText(_translate("splash_screen", "Выход"))