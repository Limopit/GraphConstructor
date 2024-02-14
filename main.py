import sys

import pyqtgraph as pg
import pyqtgraph.exporters
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtWidgets import QFileDialog

import graph as main
import windows.helpWindow as hp
import windows.errorWindow as error
import windows.authorWindow as author
import windows.programWindow as program
import windows.splashScreen as splash


class SplashWindow(QtWidgets.QMainWindow, splash.UiSplashScreen):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._setup_ui_(self)
        self.main_window = None
        self.button_next.clicked.connect(self.click)

    def click(self):
        self.close()
        self.main_window = MainWindow()
        self.main_window.show()


class MainWindow(QtWidgets.QMainWindow, main.MainWindowLogic):
    def __init__(self):
        super().__init__()
        self._setup_ui_(self)
        self.author_window = None
        self.program_window = None
        self.help_window = None
        self.error_window = None
        self.was_opened = False
        self.create_plot()
        self.button_author.clicked.connect(self.show_author)
        self.button_program.clicked.connect(self.show_program)
        self.button_help.clicked.connect(self.show_help)
        self.button_error.clicked.connect(self.show_error)
        self.save.triggered.connect(self.file_save)
        self.open.triggered.connect(self.file_open)
        self.exp_graph.triggered.connect(self.graph_exporter)

    def keyPressEvent(self, e): # Обработка нажатия кнопок клавиатуры
        if e.key() == 16777220:
            self.add_graph()
        if e.key() == 16777223:
            self.clear()

    def file_save(self): # Функция сохранения файла
        name, _ = QFileDialog.getSaveFileName(self, 'Save file', 'new_graph.txt')
        file = open(name, 'w')
        self.items = []
        for i in range(self.funclistWidget.count()):
            self.items.append(self.funclistWidget.item(i).text() + " " + self.borders[i])
        for i in range(len(self.items)):
            if i == len(self.items) - 1 or (self.was_opened and i == 0):
                file.write(self.items[i])
            else:
                file.write(self.items[i] + '\n')
        file.close()

    def file_open(self): # Функция открытия файла
        try:
            self.was_opened = True
            name, _ = QFileDialog.getOpenFileName(self, 'Open file')
            file = open(name, 'r')
            self.items = []
            self.borders = []
            with file:
                text = file.readline().split(' ')
                while text is not None:
                    self.items.append(text[0])
                    self.borders.append(text[1] + ' ' + text[2] + ' ' + text[3])
                    self.form_graph(text[0], [], [float(text[1]), float(text[2])], float(text[3]))
                    self.funclistWidget.addItem(text[0])
                    text = file.readline().split()
        except IndexError:
            pass
        except FileNotFoundError:
            pass

    def graph_exporter(self): # Функция экспорта графика
        exporter = pg.exporters.ImageExporter(self.plt.plotItem)
        name, _ = QFileDialog.getSaveFileName(self, 'Save graph', 'new_graph.png')
        exporter.export(name)

    def show_author(self):
        self.author_window = AuthorWindow()
        self.author_window.show()

    def show_program(self):
        self.program_window = ProgramWindow()
        self.program_window.show()

    def show_error(self):
        self.error_window = ErrorWindow()
        self.error_window.show()

    def show_help(self):
        self.help_window = HelpWindow()
        self.help_window.show()


class AuthorWindow(QtWidgets.QMainWindow, author.UiAuthorWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui_(self)


class ProgramWindow(QtWidgets.QMainWindow, program.UiProgramWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui_(self)


class ErrorWindow(QtWidgets.QMainWindow, error.UiErrorWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui_(self)


class HelpWindow(QtWidgets.QMainWindow, hp.UiHelpWindow):
    def __init__(self):
        super().__init__()
        self._setup_ui_(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    splash_screen = SplashWindow()
    splash_screen.show()
    QtCore.QTimer.singleShot(60000, splash_screen.close) # таймер закрытия старотового окна
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
