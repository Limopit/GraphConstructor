from PyQt6 import QtWidgets, QtCore, QtGui


class UiHelpWindow(object): # Класс, задающий параметры окна "Помощь"
    def _setup_ui_(self, help_window):
        help_window.setObjectName("help_window")
        help_window.resize(1011, 670)
        self.centralwidget = QtWidgets.QWidget(parent=help_window)
        self.centralwidget.setObjectName("centralwidget")
        self.label_help = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_help.setGeometry(QtCore.QRect(5, -15, 801, 681))
        self.label_help.setText("")
        self.label_help.setPixmap(QtGui.QPixmap("resources/help.png"))
        self.label_help.setObjectName("label_help")
        self.groupBox = QtWidgets.QGroupBox(parent=self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(809, 9, 191, 641))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_info = QtWidgets.QLabel(parent=self.groupBox)
        self.label_info.setGeometry(QtCore.QRect(10, 10, 171, 621))
        self.label_info.setObjectName("label_info")
        self.exitButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.exitButton.setGeometry(QtCore.QRect(910, 620, 75, 23))
        self.exitButton.setObjectName("exitButton")
        help_window.setCentralWidget(self.centralwidget)

        self._retranslate_ui_(help_window)
        QtCore.QMetaObject.connectSlotsByName(help_window)

        self.exitButton.clicked.connect(help_window.close)

    def _retranslate_ui_(self, help_window):
        _translate = QtCore.QCoreApplication.translate
        help_window.setWindowTitle(_translate("help_window", "Помощь"))
        self.label_info.setText(_translate("help_window", "1. Поле для ввода\n"
                                                      "    формулы графика\n"
                                                      "\n"
                                                      "2. Область изображения\n"
                                                      "     графика\n"
                                                      "\n"
                                                      "3. Шаблоны возможных\n"
                                                      "    функций (имеется \n"
                                                      "    несколько вкладок)\n"
                                                      "\n"
                                                      "4. Список построенных\n"
                                                      "    функций\n"
                                                      "\n"
                                                      "5. Панель цифр, \n"
                                                      "    операторов и \n"
                                                      "    др. символов\n"
                                                      "\n"
                                                      "6. Панель задачи\n"
                                                      "    границ и шага графика\n"
                                                      "\n"
                                                      "7. Меню для \n"
                                                      "    работы с файлами"))
        self.label_info.font().setBold(True)
        self.label_info.font().setPointSize(11)
        self.exitButton.setText(_translate("help_window", "Выход"))
