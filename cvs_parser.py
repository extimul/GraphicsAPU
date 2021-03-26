

class DataParser:
    def __init__(self, data):
        self.data = data
        # Удаляем заголовки
        self.data.pop(0)

    def parse_time_line(self):
        time_line = []
        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] == self.data[i][0]:
                    temp = str(self.data[i][j])
                    temp = temp.split(" ", 1)
                    time = temp[1]
                    time_line.append(time[:-7])

        return time_line

    def parse_acc_values(self):
        return self.__axis3template([2, 3, 4])

    def parse_gyr_values(self):
        return self.__axis3template([5, 6, 7])

    def parse_orientation_values(self):
        return self.__axis3template([8, 9, 10])

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

