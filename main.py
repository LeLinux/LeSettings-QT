import sys

import configurator as conf
import qdarktheme
from PySide6 import QtWidgets, QtGui, QtCore


class LeSettings(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        conf.main_window = self

        # тут инициализация окна и прочей хуйни

        # conf.allbtns = conf.AllButtons()

        ui = conf.UI()
        ui.setUI()



        # conf.allbtns = conf.AllButtons()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # тут сам выбери какой варик инициализации темы надо
    qdarktheme.setup_theme()
    # app.setStyleSheet(qdarkstyle.load_stylesheet())

    # font_size = conf.window_width / 800 * 12
    # app.setFont(QtGui.QFont("Ubuntu Mono", int(font_size)))

    lesettings = LeSettings()
    lesettings.setFixedSize(conf.window_width, conf.window_height)
    lesettings.show()

    sys.exit(app.exec())
