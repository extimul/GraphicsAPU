import csv
import os


class Reader:
    def __init__(self, file):
        self.file = file
        self.row_collection = None

        self.__file_is_exist()

    def __file_is_exist(self):
        if not os.path.exists(self.file):
            raise RuntimeError('Файл отсутствует')

    def read_data(self):
        row_collection = []
        with open(self.file, 'r') as f_obj:
            reader = csv.reader(f_obj)
            for row in reader:
                s = "".join(row)
                row = s.split(';')
                row_collection.append(row)

        return row_collection


# if __name__ == '__main__':
#     r = Reader('files\\BLACKBOX.csv')
#     data = r.read_data()
#
#     data.pop(0)
#
#     for i in range(len(data)):
#         for j in range(len(data[i])):
#             if data[i][j] == data[i][0]:
#                 temp = str(data[i][j])
#                 temp = temp.split(" ", 1)
#                 time = temp[1]
#                 print(time[:-4])


