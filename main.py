from PySide6 import QtCore, QtWidgets, QtGui
import sys
import configurator as conf
import qdarktheme

class LeSettings(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        QtGui.QIcon.setThemeName("candy-icons")

        conf.main_window = self
        conf.allbtns = conf.AllButtons()


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    qdarktheme.setup_theme()

    font_size = conf.window_width / 800 * 12
    app.setFont(QtGui.QFont("Ubuntu Mono", int(font_size)))

    lesettings = LeSettings()
    lesettings.setFixedSize(conf.window_width, conf.window_height)
    lesettings.show()

    sys.exit(app.exec())
