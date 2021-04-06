

class DataParser:
    def __init__(self, data):
        self.data = data
        # Удаляем заголовки
        self.data.pop(0)

    def parse_time_line(self):
        time_line = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == 0:
                    temp = str(self.data[i][j])
                    temp = temp.split(" ", 1)
                    time = temp[1]
                    time_line.append(time[:-7])

        return time_line

    def parse_acc_values(self):
        return self.__axis3template([1, 2, 3])

    def parse_gyr_values(self):
        return self.__axis3template([4, 5, 6])

    def parse_orientation_values(self):
        return self.__axis3template([7, 8, 9])

    def parse_location_values(self):
        return self.__template([10, 11])

    def parse_height_values(self):
        height_values = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == 13:
                    temp = str(self.data[i][j])
                    temp = temp.split("+", 1)
                    height = temp[1]
                    height_values.append(height)

        return height_values

    def parse_gyr_angle(self):
        return self.__axis3template([14, 15, 16])

    def parse_signal_values(self):
        signal_values = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == 12:
                    value = int(self.data[i][j])
                    signal_values.append(value)

        return signal_values

    def __axis3template(self, args):
        x_data, y_data, z_data = [], [], []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == args[0]:
                    value = float(self.data[i][j])
                    x_data.append(value)
                if j == args[1]:
                    value = float(self.data[i][j])
                    y_data.append(value)
                if j == args[2]:
                    value = float(self.data[i][j])
                    z_data.append(value)

        return x_data, y_data, z_data

    def __template(self, args):
        x_data, y_data = [], []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if j == args[0]:
                    value = float(self.data[i][j])
                    x_data.append(value)
                if j == args[1]:
                    value = float(self.data[i][j])
                    y_data.append(value)

        return x_data, y_data



