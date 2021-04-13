from dataclasses import dataclass

S_QUIT = 'Выход'
S_BACK = 'Назад'

MAIN_MENU = ['Графики', 'Настройки', S_QUIT]

SETTINGS_MENU = ['Не доступно', S_BACK]

GRAPHICS_MENU = ['Создать график линейной скорости',  'Создать график угловой скорости', 'Создать график ориентации',
                 'Создать график геолокации', 'Создать график ыыы', 'Создать график положений гиро', S_BACK]

COLORS = ['red', 'blue', 'green']


@dataclass
class GraphicsData:
    TimeLine: list[str]
    AccX: list[float]
    AccY: list[float]
    AccZ: list[float]
    GyrX: list[float]
    GyrY: list[float]
    GyrZ: list[float]
    Pitch: list[float]
    Roll: list[float]
    Yaw: list[float]
    Altitude: list[float]
    Signal: list[float]
    Elevator: list[float]
    Aileron: list[float]
    Rudder: list[float]