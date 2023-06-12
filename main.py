import sys

import configurator as conf
import qdarktheme
from PySide6 import QtWidgets, QtGui, QtCore


class LeSettings(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        conf.main_window = self

        ui = conf.UI()
        ui.setUI()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    qdarktheme.setup_theme()

    app.setFont(QtGui.QFont("Ubuntu Mono"))

    lesettings = LeSettings()
    lesettings.setFixedSize(conf.window_width, conf.window_height)
    lesettings.show()

    sys.exit(app.exec())
