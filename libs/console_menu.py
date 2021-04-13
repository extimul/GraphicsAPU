import traceback
import os

S_INPUT_INDEX = "Введите индекс: "
INVALID_INPUT_ERROR = "Некорректный ввод"
INDEX_INPUT_ERROR = "Такого пункта не существует"
INVALID_NUMBER_OF_ELEMENTS = 'Некорректное количество элементов меню и функций'


class MenuModel(object):
    def __init__(self, title, menu_elements: list, func_collection: dict):
        self.title = title
        self.menu_elements = menu_elements
        self.func_collection = func_collection

        self.__equal()

    def __equal(self):
        try:
            if len(self.menu_elements) != len(self.func_collection):
                raise RuntimeError
        except RuntimeError as ex:
            print(traceback.format_exc())
            print(ex)


class Menu:
    def __init__(self):
        self.menu_collection = []
        self.current_menu_obj = None
        self.menu_level = 0

    def start(self):
        try:
            if self.current_menu_obj is not None:
                self.menu_collection.append(self.current_menu_obj)
                self.__upd_menu_lvl()
                self.__display_menu()
            else:
                raise RuntimeError
        except RuntimeError as ex:
            print(ex)

    def go_forward(self, next_menu_obj: MenuModel):
        self.current_menu_obj = next_menu_obj
        self.menu_collection.append(self.current_menu_obj)
        self.__upd_menu_lvl()
        self.__display_menu()

    def go_back(self):
        p_level = self.menu_level - 1
        self.current_menu_obj = self.menu_collection[p_level]
        self.menu_collection.remove(self.menu_collection[self.menu_level])
        self.__upd_menu_lvl()
        self.__display_menu()

    def __display_menu(self):
        self.clear()
        if self.current_menu_obj is not None:
            print(self.current_menu_obj.title)
            for index, element in enumerate(self.current_menu_obj.menu_elements):
                print(f"{index + 1}.{element}")

            self.__wait_input(self.current_menu_obj)

    def __wait_input(self, menu_obj: MenuModel):
        state_flag = True
        while state_flag:
            try:
                user_input = int(input(S_INPUT_INDEX))
                if user_input <= len(menu_obj.func_collection):
                    # state_flag = False
                    func_dict_keys = list(menu_obj.func_collection.keys())
                    menu_obj.func_collection[func_dict_keys[user_input - 1]]()
                    self.__display_menu()
                else:
                    raise ValueError
            except ValueError:
                print(INVALID_INPUT_ERROR)

    @staticmethod
    def clear():
        os.system('cls')

    def __upd_menu_lvl(self):
        self.menu_level = len(self.menu_collection) - 1