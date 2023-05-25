from screeninfo import get_monitors
from PySide6 import QtCore, QtWidgets, QtGui

window_width = 0
window_height = 0

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
        window_width = window_width * width_const
        window_height = window_width * height_const

    print("[LOG] window size", window_width, "x", window_height)

setWindowSize()

class WidgetParamets:
    def __init__(self):

        #buttons positions of start menu
        self.start_menu_button_size = 0

        self.system_button_x = 0
        self.system_button_y = 0

        self.connections_button_x = 0
        self.connections_button_y = 0

        self.devices_button_x = 0
        self.devices_button_y = 0

        self.appearance_button_x = 0
        self.appearance_button_y = 0
        self.setStartMenuButtons()

        #buttons positions of system menu
        self.system_menu_button_size = 0

        self.language_n_region_button_x = 0
        self.language_n_region_button_y = 0

        self.date_n_time_button_x = 0
        self.date_n_time_button_y = 0

        self.sound_button_x = 0
        self.sound_button_y = 0

        self.power_button_x = 0
        self.power_button_y = 0

        self.users_button_x = 0
        self.users_button_y = 0

        self.system_info_button_x = 0
        self.system_info_button_y = 0
        self.setSystemMenuButtons()

    def setStartMenuButtons(self):
        self.start_menu_button_size = window_width / 5

        vertical_spaces = (window_height - 2 * self.start_menu_button_size) / 3

        self.system_button_x = self.start_menu_button_size
        self.system_button_y = vertical_spaces

        self.connections_button_x = self.start_menu_button_size + 2 * self.start_menu_button_size
        self.connections_button_y = vertical_spaces

        self.devices_button_x = self.system_button_x
        self.devices_button_y = self.start_menu_button_size + 2 * vertical_spaces

        self.appearance_button_x = self.connections_button_x
        self.appearance_button_y = self.devices_button_y

        print("[LOG] button size in start menu", self.start_menu_button_size)

    def setSystemMenuButtons(self):
        self.system_menu_button_size = window_width / 7

        vertical_spaces = (window_height - 2 * self.system_menu_button_size) / 3

        self.language_n_region_button_x = self.system_menu_button_size
        self.language_n_region_button_y = self.system_menu_button_size

        self.date_n_time_button_x = self.language_n_region_button_x + 2 * self.system_menu_button_size
        self.date_n_time_button_y = self.system_menu_button_size

        self.sound_button_x = self.date_n_time_button_x + 2 * self.system_menu_button_size
        self.sound_button_y = self.system_menu_button_size

        self.power_button_x = self.language_n_region_button_x
        self.power_button_y = self.language_n_region_button_y + self.system_menu_button_size + vertical_spaces

        self.users_button_x = self.date_n_time_button_x
        self.users_button_y = self.power_button_y

        self.system_info_button_x = self.sound_button_x
        self.system_info_button_y = self.power_button_y

widget_parametrs = WidgetParamets()

class AllIcons:
    def __init__(self):
        pass

main_window = None

'''
input:
    link to button
    icon name from icon theme(can be found in /usr/share/icons/ICON_THEME_NAME) or from AllIcons class
    text placed below icon
    fucntion which calls on click
    width and height of button
    position on screen(x starts from left side of screen. y start from top side of screen)
'''
def setToolButtonParametrs(button, icon_name, icon_size, text, connected_func, width, height, x_position, y_position):
    button.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
    button.setStyleSheet('QToolButton {font: 20px}')
    button.setIcon(QtGui.QIcon.fromTheme(icon_name))
    button.setIconSize(QtCore.QSize(icon_size, icon_size))
    button.setText(text)
    button.clicked.connect(connected_func)
    button.setGeometry(0, 0, width, height)
    button.move(x_position, y_position)

class SystemMenu:
    def __init__():
        self.language_n_region_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.language_n_region_button,
                               icon_name = "locale",
                               icon_size = 120,
                               text = "Langueage & Region",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.system_button_x,
                               y_position = widget_parametrs.system_button_y,
                               connected_func = None)

        self.connections_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.connections_button,
                               icon_name = "accessories-clock",
                               icon_size = 120,
                               text = "Connections",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.connections_button_x,
                               y_position = widget_parametrs.connections_button_y,
                               connected_func = None)

        self.devices_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.devices_button,
                               icon_name = "randr",
                               icon_size = 120,
                               text = "Devices",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.devices_button_x,
                               y_position = widget_parametrs.devices_button_y,
                               connected_func = None)

        self.appearance_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.appearance_button,
                               icon_name = "randr",
                               icon_size = 120,
                               text = "Appearance",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.appearance_button_x,
                               y_position = widget_parametrs.appearance_button_y,
                               connected_func = None)

        self.devices_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.devices_button,
                               icon_name = "randr",
                               icon_size = 120,
                               text = "Devices",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.devices_button_x,
                               y_position = widget_parametrs.devices_button_y,
                               connected_func = None)

        self.appearance_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.appearance_button,
                               icon_name = "randr",
                               icon_size = 120,
                               text = "Appearance",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.appearance_button_x,
                               y_position = widget_parametrs.appearance_button_y,
                               connected_func = None)

class StartMenu:
    def __init__(self):
        self.system_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.system_button,
                               icon_name = "obconf",
                               icon_size = 120,
                               text = "System",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.system_button_x,
                               y_position = widget_parametrs.system_button_y,
                               connected_func = None)

        self.connections_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.connections_button,
                               icon_name = "proxy",
                               icon_size = 120,
                               text = "Connections",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.connections_button_x,
                               y_position = widget_parametrs.connections_button_y,
                               connected_func = None)

        self.devices_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.devices_button,
                               icon_name = "randr",
                               icon_size = 120,
                               text = "Devices",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.devices_button_x,
                               y_position = widget_parametrs.devices_button_y,
                               connected_func = None)

        self.appearance_button = QtWidgets.QToolButton(main_window)
        setToolButtonParametrs(button = self.appearance_button,
                               icon_name = "randr",
                               icon_size = 120,
                               text = "Appearance",
                               width = widget_parametrs.start_menu_button_size,
                               height = widget_parametrs.start_menu_button_size,
                               x_position = widget_parametrs.appearance_button_x,
                               y_position = widget_parametrs.appearance_button_y,
                               connected_func = None)

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

class AllButtons:
    def __init__(self):
        start_menu = StartMenu()



allbtns = None
