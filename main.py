from libs.reader import Reader
from libs.graphic import Graphics
from libs.cvs_parser import DataParser
from libs.console_menu import Menu, MenuModel
from libs.strings import *

from sys import exit

from time import time
from multiprocessing import Process
FILE_PATH = 'files/logs/BLACKBOX.csv'


class GraphicsAPU:
    def __init__(self):
        self.data_parser = self.__init_data_parser()
        self.data_buffer = GraphicsData([], [], [], [], [], [], [], [], [], [], [], [], [], [], [])
        self.__init_task()

    @staticmethod
    def __init_data_parser():
        file_reader = Reader(FILE_PATH)
        raw_data = file_reader.read_data()
        return DataParser(raw_data)

    def __init_cli(self):
        pass

    def parse_time_line(self):
        self.data_buffer.TimeLine = self.data_parser.parse_time_line()

    def parse_acc_data(self):
        self.data_buffer.AccX, self.data_buffer.AccY, self.data_buffer.AccZ = self.data_parser.parse_acc_values()

    def parse_gyr_data(self):
        self.data_buffer.GyrX, self.data_buffer.GyrY, self.data_buffer.GyrZ = self.data_parser.parse_gyr_values()

    def parse_orientation_data(self):
        self.data_buffer.GyrX, self.data_buffer.GyrY, self.data_buffer.GyrZ = self.data_parser.parse_orientation_values()

    def parse_RTK_data(self):
        self.data_buffer.Signal, self.data_buffer.Altitude = self.data_parser.parse_RTK_values()

    def parse_rudders_data(self):
        self.data_buffer.Elevator, self.data_buffer.Aileron, self.data_buffer.Rudder = self.data_parser.parse_rudders_angle()

    def __init_task(self):
        start_time = time()
        funcs = [self.parse_time_line(),
                 self.parse_acc_data(),
                 self.parse_gyr_data(),
                 self.parse_orientation_data(),
                 self.parse_RTK_data(),
                 self.parse_rudders_data()]

        for i in range(len(funcs)):
            process = Process(target=funcs[i], name=f'P{i}')
            process.start()
            # process.join()

        print(f'Tasks down: {time() - start_time}')


if __name__ == '__main__':
    app = GraphicsAPU()

    # reader = Reader(FILE_PATH)
    # data = reader.read_data()
    #
    # parser = DataParser(data)
    # time_line = parser.parse_time_line()
    # gyrX_data, gyrY_data, gyrZ_data = parser.parse_gyr_values()
    # accX_data, accY_data, accZ_data = parser.parse_acc_values()
    # roll, pitch, yaw = parser.parse_orientation_values()
    # north, east = parser.parse_location_values()
    # height_data = parser.parse_height_values()
    # signal_data = parser.parse_signal_values()
    # roll_, pitch_, yaw_ = parser.parse_gyr_angle()
    #
    # graphics = Graphics(time_line)
    #
    # menu = Menu()
    #
    # main_menu = MenuModel('Главное меню', MAIN_MENU, {
    #     1: lambda: menu.go_forward(graphics_menu),
    #     2: lambda: menu.go_forward(settings_menu),
    #     3: lambda: exit()
    # })
    #
    # settings_menu = MenuModel('Настройки', SETTINGS_MENU, {
    #     1: 'Not available',
    #     2: lambda: menu.go_back()
    # })
    #
    # graphics_menu = MenuModel('Графики', GRAPHICS_MENU, {
    #     1: lambda: graphics.create_graphic("acc_graphic", [accX_data, accY_data, accZ_data, 'AccX', 'AccY', 'AccZ']),
    #     2: lambda: graphics.create_graphic("gyr_graphic", [gyrX_data, gyrY_data, gyrZ_data, 'GyrX', 'GyrY', 'GyrZ']),
    #     3: lambda: graphics.create_graphic("orientation_graphic", [roll, pitch, yaw, 'Roll', 'Pitch', 'Yaw']),
    #     4: lambda: graphics.create_graphic("location_graphic", [north, east, 'North', 'East']),
    #     5: lambda: graphics.create_graphic("sh_graphic", [height_data, signal_data, 'Height', 'Signal']),
    #     6: lambda: graphics.create_graphic("Gyro angels", [roll_, pitch_, yaw_, 'Roll', 'Pitch', 'Yaw']),
    #     7: lambda: menu.go_back()
    # })
    #
    # menu.current_menu_obj = main_menu
    # menu.start()



