from reader import Reader
from graphic import APUGraphic
from cvs_parser import DataParser
from helpers.console_menu import Menu, MenuModel
from helpers.strings import *

from time import time
from sys import exit

FILE_PATH = 'files/logs/BLACKBOX.csv'

if __name__ == '__main__':

    reader = Reader(FILE_PATH)
    data = reader.read_data()

    parser = DataParser(data)

    start_time = time()
    time_line = parser.parse_time_line()
    gyrX_data, gyrY_data, gyrZ_data = parser.parse_gyr_values()
    accX_data, accY_data, accZ_data = parser.parse_acc_values()
    roll, pitch, yaw = parser.parse_orientation_values()
    north, east = parser.parse_location_values()
    height_data = parser.parse_height_values()
    signal_data = parser.parse_signal_values()
    roll_, pitch_, yaw_ = parser.parse_gyr_angle()

    print(f'Parse is end: {time() - start_time}')

    graphics = APUGraphic(time_line)

    menu = Menu()

    main_menu = MenuModel('Главное меню', MAIN_MENU, {
        1: lambda: menu.go_forward(graphics_menu),
        2: lambda: menu.go_forward(settings_menu),
        3: lambda: exit()
    })

    settings_menu = MenuModel('Настройки', SETTINGS_MENU, {
        1: 'Not available',
        2: lambda: menu.go_back()
    })

    graphics_menu = MenuModel('Графики', GRAPHICS_MENU, {
        1: lambda: graphics.create_graphic("acc_graphic", [accX_data, accY_data, accZ_data, 'AccX', 'AccY', 'AccZ']),
        2: lambda: graphics.create_graphic("gyr_graphic", [gyrX_data, gyrY_data, gyrZ_data, 'GyrX', 'GyrY', 'GyrZ']),
        3: lambda: graphics.create_graphic("orientation_graphic", [roll, pitch, yaw, 'Roll', 'Pitch', 'Yaw']),
        4: lambda: graphics.create_graphic("location_graphic", [north, east, 'North', 'East']),
        5: lambda: graphics.create_graphic("sh_graphic", [height_data, signal_data, 'Height', 'Signal']),
        6: lambda: graphics.create_graphic("Gyro angels", [roll_, pitch_, yaw_, 'Roll', 'Pitch', 'Yaw']),
        7: lambda: menu.go_back()
    })

    menu.current_menu_obj = main_menu
    menu.start()



