import random

import numexpr as ne
import numpy as np
import pyqtgraph as pg
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QMessageBox

import windows.mainWindow as main


class MainWindowLogic(main.UiMainWindow):  # Класс, содержащий логику работы главного окна
    def _setup_ui_(self, mainWindow):

        main.UiMainWindow._setup_ui_(self, mainWindow)

        self.buttons_clicked()                                      # Обработка нажатия кнопок окна
        self.button_add.clicked.connect(self.add_graph)
        self.button_clear.clicked.connect(self.clear)
        self.button_exit.clicked.connect(mainWindow.close)

        lay = QtWidgets.QVBoxLayout(self.label_graph)               # Создание поля графика
        lay.setContentsMargins(0, 0, 0, 0)
        self.plt = pg.plot()
        lay.addWidget(self.plt)

        self.items = []
        self.borders = []

    def buttons_clicked(self):  # Метод обработки нажатия кнопок окна
        self.button_zero.clicked.connect(lambda: self.add_to_formula(self.button_zero.text()))
        self.button_one.clicked.connect(lambda: self.add_to_formula(self.button_one.text()))
        self.button_two.clicked.connect(lambda: self.add_to_formula(self.button_two.text()))
        self.button_three.clicked.connect(lambda: self.add_to_formula(self.button_three.text()))
        self.button_four.clicked.connect(lambda: self.add_to_formula(self.button_four.text()))
        self.button_five.clicked.connect(lambda: self.add_to_formula(self.button_five.text()))
        self.button_six.clicked.connect(lambda: self.add_to_formula(self.button_six.text()))
        self.button_seven.clicked.connect(lambda: self.add_to_formula(self.button_seven.text()))
        self.button_eight.clicked.connect(lambda: self.add_to_formula(self.button_eight.text()))
        self.button_nine.clicked.connect(lambda: self.add_to_formula(self.button_nine.text()))
        self.button_plus.clicked.connect(lambda: self.add_to_formula(self.button_plus.text()))
        self.button_minus.clicked.connect(lambda: self.add_to_formula(self.button_minus.text()))
        self.button_mult.clicked.connect(lambda: self.add_to_formula(self.button_mult.text()))
        self.button_div.clicked.connect(lambda: self.add_to_formula(self.button_div.text()))
        self.button_dot.clicked.connect(lambda: self.add_to_formula(self.button_dot.text()))
        self.button_grade.clicked.connect(lambda: self.add_to_formula(self.button_grade.text()))
        self.button_brack_l.clicked.connect(lambda: self.add_to_formula(self.button_brack_l.text()))
        self.button_brack_r.clicked.connect(lambda: self.add_to_formula(self.button_brack_r.text()))
        self.button_abs.clicked.connect(lambda: self.add_to_formula(self.button_abs.text()))
        self.button_ln.clicked.connect(lambda: self.add_to_formula(self.button_ln.text()))
        self.button_log.clicked.connect(lambda: self.add_to_formula(self.button_log.text()))
        self.button_lg.clicked.connect(lambda: self.add_to_formula(self.button_lg.text()))
        self.button_exp.clicked.connect(lambda: self.add_to_formula(self.button_exp.text()))
        self.button_sqrt.clicked.connect(lambda: self.add_to_formula(self.button_sqrt.text()))
        self.button_sq.clicked.connect(lambda: self.add_to_formula(self.button_sq.text()))
        self.button_cube.clicked.connect(lambda: self.add_to_formula(self.button_cube.text()))
        self.button_sin.clicked.connect(lambda: self.add_to_formula(self.button_sin.text()))
        self.button_asin.clicked.connect(lambda: self.add_to_formula(self.button_asin.text()))
        self.button_cos.clicked.connect(lambda: self.add_to_formula(self.button_cos.text()))
        self.button_acos.clicked.connect(lambda: self.add_to_formula(self.button_acos.text()))
        self.button_tg.clicked.connect(lambda: self.add_to_formula(self.button_tg.text()))
        self.button_atg.clicked.connect(lambda: self.add_to_formula(self.button_atg.text()))
        self.button_ctg.clicked.connect(lambda: self.add_to_formula(self.button_ctg.text()))

    def add_to_formula(self, num):  # Метод, добаляющий текст в поле для ввода формул
        self.lineEdit_formula.setText(self.lineEdit_formula.text() + num)

    def clear(self):  # Очистка графиков
        self.funclistWidget.clear()
        self.plt.clear()
        self.items = []
        self.borders = []

    def add_graph(self):  # Добавление графика на поле
        try:
            legend = []
            limits = [float(self.lineEdit_border_x1.text()), float(self.lineEdit_border_x2.text())]
            formula = self.lineEdit_formula.text()

            self.form_graph(formula, legend, limits, float(self.step_lineEdit.text()))
            self.funclistWidget.addItem(formula)
            border_elem = (self.lineEdit_border_x1.text() + ' ' + self.lineEdit_border_x2.text()
                           + ' ' + self.step_lineEdit.text())
            self.borders.append(border_elem)

            self.plt.setXRange(limits[0] - 2, limits[1] + 2)
        except ValueError: # Обработчик неправильного ввода данных
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Critical)
            msg.setText("Ошибка данных!")
            msg.setInformativeText('Данные для формулы введены некорректно')
            msg.setWindowTitle("Ошибка")
            msg.exec()

    def form_graph(self, func, legend, limits, step):  # Формирование графика
        try:
            left_limit = limits[0]
            right_limit = limits[1] + 1
            legend.append('y=' + str(func))
            x_points = np.arange(left_limit, right_limit, step)
            y = []
            func = func.replace('^', '**').strip() # Замена элемента строки на подходящий библиотеке
            func = func.replace('X', 'x')
            func = func.replace(' ', '')
            func = func.replace('tg(x)', 'tan(x)')
            func = func.replace('arctg(x)', 'atan(x)')
            func = func.replace('ctg(x)', 'cot(x)')
            func = func.replace('|x|', 'abs(x)')
            func = func.replace('ln(x)', 'log1p(x)')
            func = func.replace('lg(x)', 'log10(x)')

            for x in x_points:
                y.append(ne.evaluate(func))
            line = self.plt.plot(x_points, y, pen=random.randint(1, 7), symbol=random.randint(1, 7),
                                symbolPen=random.randint(1, 7), symbolBrush=0.2, name=func)
            self.plt.setYRange(y[0], y[len(y) - 1])
            return line
        except Exception:
            pass

    def create_plot(self):  # Настойка пустого поля графиков
        title = "Function graph"
        y = []
        x = []

        self.plt.showGrid(x=True, y=True)

        self.plt.addLegend()

        self.plt.setLabel("left", "Y values")

        self.plt.setLabel("bottom", "X values")

        self.plt.setXRange(0, 10)

        self.plt.setYRange(0, 10)

        self.plt.setWindowTitle(title)
