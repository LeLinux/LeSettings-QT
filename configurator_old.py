from screeninfo import get_monitors
from PySide6 import QtCore, QtWidgets, QtGui
import json5 as json


window_width = 0
window_height = 0

main_window = None

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

setWindowSize()

def createConfig():
    global window_width, window_height

    #vertical_spaces = (window_height - 2 * self.start_menu_button_size) / 3
    default_button_size = window_width / 5
    size_сoeff = window_width / 800
    print(size_сoeff)

    #I wrote it 26 may of 2023. I think in few days it will be legacy code. All of this shit based on size coefficients. Nums setted first - size/coordinates in 800x600 window size
    config = {
        "back_button_width" : 60 * size_сoeff,
        "back_button_height" : 30 * size_сoeff,
        "main_menu": {
            "start_menu_button_size" : 160 * size_сoeff,
            "start_menu_icon_size" : 128 * size_сoeff,

            "system_button_x" : 160 * size_сoeff,
            "system_button_y" : 93.3 * size_сoeff,
            "system_button_text" : "System",

            "connections_button_x" : 480 * size_сoeff,
            "connections_button_y" : 93.3 * size_сoeff,
            "connections_button_text" : "Connections",

            "devices_button_x" : 160 * size_сoeff,
            "devices_button_y" : 346.6 * size_сoeff,
            "devices_button_text" : "Devices",

            "appearance_button_x" : 480 * size_сoeff,
            "appearance_button_y" : 346.6 * size_сoeff,
            "appearance_button_text" : "Appearance",
        },
        "system_menu":{
            "system_menu_button_size" : 160 * size_сoeff,
            "system_menu_icon_size" : 102.4 * size_сoeff,

            "language_n_region_button_x" : 80 * size_сoeff,
            "language_n_region_button_y" : 93.3 * size_сoeff,
            "language_n_region_button_text" : "Language &&\nRegion",

            "date_n_time_button_x" : 320 * size_сoeff,
            "date_n_time_button_y" : 93.3 * size_сoeff,
            "date_n_time_button_text" : "Date &&\nTime",

            "sound_button_x" :  560 * size_сoeff,
            "sound_button_y" : 93.3 * size_сoeff,
            "sound_button_text" :  "Sound",

            "power_button_x" : 80 * size_сoeff,
            "power_button_y" : 346.6 * size_сoeff,
            "power_button_text" : "Power",

            "users_button_x" : 320 * size_сoeff,
            "users_button_y" : 346.6 * size_сoeff,
            "users_button_text" : "Users",

            "system_info_button_x" : 560 * size_сoeff,
            "system_info_button_y" : 346.6 * size_сoeff,
            "system_info_button_text" : "System Info",
            "language_n_region":{
                "language_list_width" : 150 * size_сoeff,
                "language_list_height" : 30 * size_сoeff,
                "language_list_x" : 490 * size_сoeff,
                "language_list_y" : 200 * size_сoeff,

                "region_list_width" : 150 * size_сoeff,
                "region_list_height" : 30 * size_сoeff,
                "region_list_x" : 490 * size_сoeff,
                "region_list_y" : 300 * size_сoeff
            }
        }
    }
    with open("config.json", "w") as write_file:
        json.dump(config, write_file)

createConfig()

class WidgetParamets:
    def __init__(self):

        with open("config.json", "r") as read_file:
            config = json.load(read_file)

        self.back_button_width = config["back_button_width"]
        self.back_button_height = config["back_button_height"]

        #buttons positions of main menu
        self.start_menu_button_size = config["main_menu"]["start_menu_button_size"]
        self.start_menu_icon_size = config["main_menu"]["start_menu_icon_size"]

        self.system_button_x = config["main_menu"]["system_button_x"]
        self.system_button_y = config["main_menu"]["system_button_y"]
        self.system_button_text = config["main_menu"]["system_button_text"]

        self.connections_button_x = config["main_menu"]["connections_button_x"]
        self.connections_button_y = config["main_menu"]["connections_button_y"]
        self.connections_button_text = config["main_menu"]["connections_button_text"]

        self.devices_button_x = config["main_menu"]["devices_button_x"]
        self.devices_button_y = config["main_menu"]["devices_button_y"]
        self.devices_button_text = config["main_menu"]["devices_button_text"]

        self.appearance_button_x = config["main_menu"]["appearance_button_x"]
        self.appearance_button_y = config["main_menu"]["appearance_button_y"]
        self.appearance_button_text = config["main_menu"]["appearance_button_text"]

        #buttons positions of system menu
        self.system_menu_button_size = config["system_menu"]["system_menu_button_size"]
        self.system_menu_icon_size = config["system_menu"]["system_menu_icon_size"]


        self.language_n_region_button_x = config["system_menu"]["language_n_region_button_x"]
        self.language_n_region_button_y = config["system_menu"]["language_n_region_button_y"]
        self.language_n_region_button_text = config["system_menu"]["language_n_region_button_text"]

        self.date_n_time_button_x = config["system_menu"]["date_n_time_button_x"]
        self.date_n_time_button_y = config["system_menu"]["date_n_time_button_y"]
        self.date_n_time_button_text = config["system_menu"]["date_n_time_button_text"]

        self.sound_button_x = config["system_menu"]["sound_button_x"]
        self.sound_button_y = config["system_menu"]["sound_button_y"]
        self.sound_button_text = config["system_menu"]["sound_button_text"]

        self.power_button_x = config["system_menu"]["power_button_x"]
        self.power_button_y = config["system_menu"]["power_button_y"]
        self.power_button_text = config["system_menu"]["power_button_text"]

        self.users_button_x = config["system_menu"]["users_button_x"]
        self.users_button_y = config["system_menu"]["users_button_y"]
        self.users_button_text = config["system_menu"]["users_button_text"]

        self.system_info_button_x = config["system_menu"]["system_info_button_x"]
        self.system_info_button_y = config["system_menu"]["system_info_button_y"]
        self.system_info_button_text = config["system_menu"]["system_info_button_text"]

        #language and region menu
        self.language_list_width = config["system_menu"]["language_n_region"]["language_list_width"]
        self.language_list_height = config["system_menu"]["language_n_region"]["language_list_height"]
        self.language_list_x = config["system_menu"]["language_n_region"]["language_list_x"]
        self.language_list_y = config["system_menu"]["language_n_region"]["language_list_y"]

        self.region_list_width = config["system_menu"]["language_n_region"]["region_list_width"]
        self.region_list_height = config["system_menu"]["language_n_region"]["region_list_height"]
        self.region_list_x = config["system_menu"]["language_n_region"]["region_list_x"]
        self.region_list_y = config["system_menu"]["language_n_region"]["region_list_y"]


widget_parametrs = WidgetParamets()

'''
input:
    link to button
    icon name from icon theme(can be found in /usr/share/icons/ICON_THEME_NAME) or from AllIcons class
    text placed below icon
    fucntion which calls on click
    width and height of button
    position on screen(x starts from left side of screen. y start from top side of screen)
'''
def setToolButtonParametrs(button, icon_name, icon_size, text, connected_func, width, height, x_position, y_position, **args):
    button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    button.setIcon(QtGui.QIcon.fromTheme(icon_name))
    button.setIconSize(QtCore.QSize(icon_size, icon_size))
    button.setText(text)
    button.clicked.connect(connected_func)
    button.setGeometry(0, 0, width, height)
    button.move(x_position, y_position)

def setComboBoxParametrs(combobox, items, width, height, x_position, y_position, connected_func):
    for i in items: combobox.addItem(i)
    combobox.setGeometry(0, 0, width, height)
    combobox.move(x_position, y_position)
    combobox.activated.connect(connected_func)

class LanguageNRegion:
    def __init__(self):
        self.languages = ["Chinese", "English", "Russian"]
        self.language_list = QtWidgets.QComboBox(main_window)
        setComboBoxParametrs(self.language_list,
                             self.languages,
                             widget_parametrs.language_list_width,
                             widget_parametrs.language_list_height,
                             widget_parametrs.language_list_x,
                             widget_parametrs.language_list_y,
                             None)

        self.regions = ["Europe/Moscow", "Europe/Minsk"]
        self.region_list = QtWidgets.QComboBox(main_window)
        setComboBoxParametrs(self.region_list,
                             self.regions,
                             widget_parametrs.region_list_width,
                             widget_parametrs.region_list_height,
                             widget_parametrs.region_list_x,
                             widget_parametrs.region_list_y,
                             None)

class SystemMenu:
    def __init__(self):
        self.language_n_region_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.language_n_region_button,
                               icon_name = "locale",
                               icon_size = widget_parametrs.system_menu_icon_size,
                               text = widget_parametrs.language_n_region_button_text,
                               width = widget_parametrs.system_menu_button_size,
                               height = widget_parametrs.system_menu_button_size,
                               x_position = widget_parametrs.language_n_region_button_x,
                               y_position = widget_parametrs.language_n_region_button_y,
                               connected_func = None)

        self.date_n_time_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.date_n_time_button,
                               icon_name = "accessories-clock",
                               icon_size = widget_parametrs.system_menu_icon_size,
                               text = widget_parametrs.date_n_time_button_text,
                               width = widget_parametrs.system_menu_button_size,
                               height = widget_parametrs.system_menu_button_size,
                               x_position = widget_parametrs.date_n_time_button_x,
                               y_position = widget_parametrs.date_n_time_button_y,
                               connected_func = None)

        self.sound_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.sound_button,
                               icon_name = "kmix",
                               icon_size = widget_parametrs.system_menu_icon_size,
                               text = widget_parametrs.sound_button_text,
                               width = widget_parametrs.system_menu_button_size,
                               height = widget_parametrs.system_menu_button_size,
                               x_position = widget_parametrs.sound_button_x,
                               y_position = widget_parametrs.sound_button_y,
                               connected_func = None)

        self.power_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.power_button,
                               icon_name = "cs-power",
                               icon_size = widget_parametrs.system_menu_icon_size,
                               text = widget_parametrs.power_button_text,
                               width = widget_parametrs.system_menu_button_size,
                               height = widget_parametrs.system_menu_button_size,
                               x_position = widget_parametrs.power_button_x,
                               y_position = widget_parametrs.power_button_y,
                               connected_func = None)

        self.users_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.users_button,
                               icon_name = "preferences-system-users",
                               icon_size = widget_parametrs.system_menu_icon_size,
                               text = widget_parametrs.users_button_text,
                               width = widget_parametrs.system_menu_button_size,
                               height = widget_parametrs.system_menu_button_size,
                               x_position = widget_parametrs.users_button_x,
                               y_position = widget_parametrs.users_button_y,
                               connected_func = None)

        self.system_info_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.system_info_button,
                               icon_name = "lbry",
                               icon_size = widget_parametrs.system_menu_icon_size,
                               text = widget_parametrs.system_info_button_text,
                               width = widget_parametrs.system_menu_button_size,
                               height = widget_parametrs.system_menu_button_size,
                               x_position = widget_parametrs.system_info_button_x,
                               y_position = widget_parametrs.system_info_button_y,
                               connected_func = None)

    def hide(self):
        self.language_n_region_button.hide()
        self.date_n_time_button.hide()
        self.sound_button.hide()
        self.power_button.hide()
        self.users_button.hide()
        self.system_info_button.hide()

    def show(self):
        self.language_n_region_button.show()
        self.date_n_time_button.show()
        self.sound_button.show()
        self.power_button.show()
        self.users_button.show()
        self.system_info_button.show()

class StartMenu:
    def __init__(self):
        self.system_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.system_button,
                               icon_name = "obconf",
                               icon_size = widget_parametrs.start_menu_icon_size,
                               text = widget_parametrs.system_button_text,
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.system_button_x,
                               y_position = widget_parametrs.system_button_y,
                               connected_func = lambda: self.show_system_menu())

        self.connections_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.connections_button,
                               icon_name = "proxy",
                               icon_size = widget_parametrs.start_menu_icon_size,
                               text = widget_parametrs.connections_button_text,
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.connections_button_x,
                               y_position = widget_parametrs.connections_button_y,
                               connected_func = None)

        self.devices_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.devices_button,
                               icon_name = "randr",
                               icon_size = widget_parametrs.start_menu_icon_size,
                               text = widget_parametrs.devices_button_text,
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.devices_button_x,
                               y_position = widget_parametrs.devices_button_y,
                               connected_func = None)

        self.appearance_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.appearance_button,
                               icon_name = "xfce4-backdrop",
                               icon_size = widget_parametrs.start_menu_icon_size,
                               text = widget_parametrs.appearance_button_text,
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.appearance_button_x,
                               y_position = widget_parametrs.appearance_button_y,
                               connected_func = None)

        self.back = QtWidgets.QToolButton(main_window)
        self.back.hide()

        self.system_menu = SystemMenu()
        self.system_menu.hide()

    def hide(self):
        self.system_button.hide()
        self.connections_button.hide()
        self.devices_button.hide()
        self.appearance_button.hide()

    def show(self):
        self.system_button.show()
        self.connections_button.show()
        self.devices_button.show()
        self.appearance_button.show()

    def back_to_system_menu(self, child_class):
        self.show()
        child_class.hide()
        self.back.hide()

    def show_system_menu(self):
        self.hide()
        self.system_menu.show()
        setToolButtonParametrs(button = self.back,
                               icon_name = None,
                               icon_size = widget_parametrs.start_menu_icon_size,
                               text = "< Back",
                               width = widget_parametrs.back_button_width,
                               height = widget_parametrs.back_button_height,
                               x_position = 0,
                               y_position = 0,
                               connected_func = lambda : self.back_to_system_menu(self.system_menu))
        self.back.show()


class AllButtons:
    def __init__(self):
        start_menu = StartMenu()
        sss = LanguageNRegion()
        #start_menu.hide_start_menu()
        #sss = SystemMenu()


allbtns = None
