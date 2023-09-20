import sys

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import pyqtSlot
from .fastserial_gui import Ui_MainWindow as FastSerial_Ui

class FastSerialGUI(QMainWindow, FastSerial_Ui):
    def __init__(self):
        QMainWindow.__init__(self)
        FastSerial_Ui.__init__(self)
        self.setupUi(self)

    @pyqtSlot()
    def port_selected(self, index: int) -> None:
        pass

    @pyqtSlot()
    def refresh_port_list(self) -> None:
        pass

    @pyqtSlot()
    def connect_to_port(self) -> None:
        pass

    @pyqtSlot()
    def set_baud_rate(self) -> None:
        pass


def start_gui():
    app = QApplication([])
    window = FastSerialGUI()
    window.show()
    sys.exit(app.exec())
