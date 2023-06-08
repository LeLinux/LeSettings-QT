from screeninfo import get_monitors
from PySide6 import QtCore, QtWidgets, QtGui
import json5 as json

main_window = None

window_width = 0
window_height = 0

class _init_magic:
    def hide():
        pass
active_menu = _init_magic

def setWindowSize():
    global window_width
    global window_height
    window = get_monitors()
    for i in range(len(window)):
        if window_width < window[i].width:
            window_width = window[i].width
            window_height = window[i].height

    width_const = 0.417
    height_const = 0.31275

    print("[LOG] display size" , window_width, "x", window_height)

    if window_width <= 1920 and window_height <= 1080:
        window_width = 800
        window_height = 600
    else:
        window_width_clone = window_width
        window_width = window_width * width_const
        window_height = window_width_clone * height_const

    print("[LOG] window size", window_width, "x", window_height)

def setComboBoxParametrs(combobox, items, width, height, x_position, y_position, connected_func):
    for i in items: combobox.addItem(i)
    combobox.setGeometry(0, 0, width, height)
    combobox.move(x_position, y_position)
    combobox.activated.connect(connected_func)

setWindowSize()

class WIFI_menu:
    def __init__(self):
        pass

class Ethernet_menu:
    def __init__(self):
        pass

class BlueTooth_menu:
    def __init__(self):
        pass

class Language_and_Region_menu:
    def __init__(self):
        self.languages = ["Chinese", "English", "Russian"]
        self.language_list = QtWidgets.QComboBox(main_window)
        setComboBoxParametrs(self.language_list,
                             self.languages,
                             160,
                             30,
                             window_width / 3,
                             window_height / 5,
                             None)

        self.regions = ["Europe/Moscow", "Europe/Minsk"]
        self.region_list = QtWidgets.QComboBox(main_window)
        # setComboBoxParametrs(self.region_list,
        #                      self.regions,
        #                      widget_parametrs.region_list_width,
        #                      widget_parametrs.region_list_height,
        #                      widget_parametrs.region_list_x,
        #                      widget_parametrs.region_list_y,
        #                      None)
        self.hide()

    def show(self):
        self.language_list.show()
        self.region_list.show()

    def hide(self):
        self.language_list.hide()
        self.region_list.hide()

class UI:
    def setUI(self):
        QtGui.QIcon.setThemeName("candy-icons")

        self.menu_buttons_list = QtWidgets.QListWidget(main_window)
        self.menu_buttons_list.setFixedSize(window_width / 5, window_height)

        # self.listWidgetItem = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(self.listWidgetItem)
        # self.listWidget.setItemWidget(self.listWidgetItem, self.language_list)
        #
        #
        # self.listWidgetItem1 = QtWidgets.QListWidgetItem()
        # self.listWidget.addItem(self.listWidgetItem1)
        # self.listWidget.setItemWidget(self.listWidgetItem1, self.language_list1)
        self.connections_label = QtWidgets.QLabel()
        self.connections_label.setText("Wi-Fi")
        self.connections_label.setStyleSheet("QToolButton {padding-left : 30px; }")

        self.connections_label_widget_item = QtWidgets.QListWidgetItem()
        self.connections_label_widget_item.setSizeHint(QtCore.QSize(0, 30))
        self.menu_buttons_list.addItem(self.connections_label_widget_item)
        self.menu_buttons_list.setItemWidget(self.connections_label_widget_item, self.connections_label)

        self.wifi_menu_button = QtWidgets.QToolButton()
        self.wifi_menu_button.setText("Wi-Fi")
        self.wifi_menu_button.setIcon(QtGui.QIcon.fromTheme("spotify"))
        self.wifi_menu_button.setIconSize(QtCore.QSize(24, 24))
        self.wifi_menu_button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.wifi_menu_button.setStyleSheet("QToolButton {padding-left : 5px; }")

        self.wifi_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.wifi_button_list_widget_item.setSizeHint(QtCore.QSize(0, 30))
        self.menu_buttons_list.addItem(self.wifi_button_list_widget_item)
        self.menu_buttons_list.setItemWidget(self.wifi_button_list_widget_item, self.wifi_menu_button)

        #self.listWidget.addWidget(language_list1)
