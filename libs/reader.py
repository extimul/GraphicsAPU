from csv import reader
from os.path import exists


class Reader:
    def __init__(self, file):
        self.file = file
        self.row_collection = None

        self.__file_is_exist()

    def __file_is_exist(self):
        if not exists(self.file):
            raise RuntimeError('Файл отсутствует')

    def read_data(self):
        row_collection = []
        with open(self.file, 'r') as f_obj:
            stream = reader(f_obj)
            for row in stream:
                s = "".join(row)
                row = s.split(';')
                row_collection.append(row)

        return row_collection


