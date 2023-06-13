from screeninfo import get_monitors
from PySide6 import QtCore, QtWidgets, QtGui
import custom_widgets
import json5 as json
import subprocess as sb
import spinner


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

def setSwitchSize():
    global window_width
    global window_height
    custom_widgets.switch_button_width = window_width / 26
    custom_widgets.switch_button_height = window_height / 35

def setComboBoxParametrs(combobox, items, width, height, x_position, y_position, connected_func):
    for i in items: combobox.addItem(i)
    combobox.setGeometry(0, 0, width, height)
    combobox.move(x_position, y_position)
    combobox.activated.connect(connected_func)

setWindowSize()
setSwitchSize()

class WIFI_menu:
    def __init__(self):

        self.wifi_switch = custom_widgets.SwitchButton(main_window)

        #It's just fast legacy fix. Maybe in far future I'll make normal fix
        self.wifi_switch.setChecked(1)
        self.wifi_switch.setChecked(0)

        self.wifi_switch.checkedChanged.connect(lambda : print(1))
        self.wifi_switch.move(window_width - 180 - custom_widgets.switch_button_width, window_height / 16)

        self.wifi_label = QtWidgets.QLabel(main_window)
        self.wifi_label.setFixedWidth(300)
        self.wifi_label.setText("Wi-Fi")
        self.wifi_label.setStyleSheet("QLabel {font-size: 18px;}")

        self.wifi_label.move(390, window_height / 16)


        self.wifi_list = QtWidgets.QListWidget(main_window)
        self.wifi_list.setFixedSize(497, 400)
        self.wifi_list.move(390, window_height / 5)

        #print(sb.check_output(["timeout", "5s", "nmcli", "-f", "SSID", "dev", "wifi"]).decode("utf-8").split("\n")[1:])
        self.spinner = spinner.WaitingSpinner(main_window)
        self.spinner.move(500, 200)
        self.spinner.start()


        self.hide()

    def search4wifi(self):
        pass

    def show(self):
        self.wifi_switch.show()
        self.wifi_label.show()

    def hide(self):
        self.wifi_switch.hide()
        self.wifi_label.hide()


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

        self.wifi_menu = WIFI_menu()

        self.connections_label = QtWidgets.QLabel()
        self.connections_label_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuLabel(self.connections_label, self.connections_label_list_widget_item, "Connections")

        self.wifi_menu_button = QtWidgets.QToolButton()
        self.wifi_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.wifi_menu_button, self.wifi_button_list_widget_item, "Wi-Fi", "spotify")
        self.wifi_menu_button.clicked.connect(lambda : self.wifi_menu.show())

        self.bluetooth_menu_button = QtWidgets.QToolButton()
        self.bluetooth_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.bluetooth_menu_button, self.bluetooth_button_list_widget_item, "Bluetooth", "bluetooth")

        self.ethenet_menu_button = QtWidgets.QToolButton()
        self.ethenet_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.ethenet_menu_button, self.ethenet_button_list_widget_item, "Ethernet", "preferences-system-network-ethernet")



        self.appearance_label = QtWidgets.QLabel()
        self.appearance_label_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuLabel(self.appearance_label, self.appearance_label_list_widget_item, "Appearance")

        self.desktop_menu_button = QtWidgets.QToolButton()
        self.desktop_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.desktop_menu_button, self.desktop_button_list_widget_item, "Desktop", "preferences-desktop-wallpaper")

        self.multitasking_menu_button = QtWidgets.QToolButton()
        self.multitasking_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.multitasking_menu_button, self.multitasking_button_list_widget_item, "Multitasking", "cs-themes")

        self.themes_menu_button = QtWidgets.QToolButton()
        self.themes_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.themes_menu_button, self.themes_button_list_widget_item, "Themes", "preferences-theme")





        self.system_label = QtWidgets.QLabel()
        self.system_label_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuLabel(self.system_label, self.system_label_list_widget_item, "System")

        self.language_and_region_menu_button = QtWidgets.QToolButton()
        self.language_and_region_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.language_and_region_menu_button, self.language_and_region_button_list_widget_item, "Language && Region", "config-language")

        self.date_and_time_menu_button = QtWidgets.QToolButton()
        self.date_and_time_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.date_and_time_menu_button, self.date_and_time_button_list_widget_item, "Date && Time", "clock")

        self.sound_menu_button = QtWidgets.QToolButton()
        self.sound_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.sound_menu_button, self.sound_button_list_widget_item, "Sound", "gnome-mixer")

        self.power_menu_button = QtWidgets.QToolButton()
        self.power_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.power_menu_button, self.power_button_list_widget_item, "Power", "preferences-system-power")

        self.users_menu_button = QtWidgets.QToolButton()
        self.user_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.users_menu_button, self.user_button_list_widget_item, "Users", "preferences-system-users")

        self.system_info_menu_button = QtWidgets.QToolButton()
        self.system_info_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.system_info_menu_button, self.system_info_button_list_widget_item, "System info", "lbry")


        self.devices_label = QtWidgets.QLabel()
        self.devices_label_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuLabel(self.devices_label, self.devices_label_list_widget_item, "Devices")

        self.displays_menu_button = QtWidgets.QToolButton()
        self.displays_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.displays_menu_button, self.displays_button_list_widget_item, "Displays", "display-capplet")

        self.keyboard_menu_button = QtWidgets.QToolButton()
        self.keyboard_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.keyboard_menu_button, self.keyboard_button_list_widget_item, "Keyboard", "input-keyboard")

        self.mouse_menu_button = QtWidgets.QToolButton()
        self.mouse_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.mouse_menu_button, self.mouse_button_list_widget_item, "Mouse", "input-mouse")

        self.printers_menu_button = QtWidgets.QToolButton()
        self.printers_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.printers_menu_button, self.printers_button_list_widget_item, "Printers", "cs-printer")

        self.drivers_menu_button = QtWidgets.QToolButton()
        self.drivers_button_list_widget_item = QtWidgets.QListWidgetItem()
        self.configureMenuButton(self.drivers_menu_button, self.drivers_button_list_widget_item, "Drivers", "driver-manager")

        self.test = QtWidgets.QToolButton()
        self.test_item = QtWidgets.QListWidgetItem()
        self.test.setText("1234")
        self.test.setIcon(QtGui.QIcon("./arrows-rotate-solid.svg"))
        self.test.setIconSize(QtCore.QSize(23, 23))
        self.test.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        self.test.setStyleSheet("QToolButton {padding-left : 5px; font-size: 16px;}")
        self.test_item.setSizeHint(QtCore.QSize(0, 30))
        self.menu_buttons_list.addItem(self.test_item)
        self.menu_buttons_list.setItemWidget(self.test_item, self.test)



    def configureMenuLabel(self, label, list_item, text):
        label.setText(text)
        label.setStyleSheet("QLabel {padding-left : 5px; font-size: 18px; background-color: #292B2E}")
        list_item.setSizeHint(QtCore.QSize(0, 30))
        self.menu_buttons_list.addItem(list_item)
        self.menu_buttons_list.setItemWidget(list_item, label)

    def configureMenuButton(self, button, list_item, text, icon_name):
        button.setText(text)
        button.setIcon(QtGui.QIcon.fromTheme(icon_name))
        button.setIconSize(QtCore.QSize(23, 23))
        button.setToolButtonStyle(QtCore.Qt.ToolButtonTextBesideIcon)
        button.setStyleSheet("QToolButton {padding-left : 5px; font-size: 16px;}")
        list_item.setSizeHint(QtCore.QSize(0, 30))
        self.menu_buttons_list.addItem(list_item)
        self.menu_buttons_list.setItemWidget(list_item, button)
