from typing import List

X_LST: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
Y_LST: List[str] = ['1', '2', '3', '4', '5', '6', '7', '8']
CLR: List[str] = ['black', 'white']


def input_cord():
    """
    функция для ввода в консоли координатов шахмоьной доски.
    проверяет в цикле корректный ввод, пока не будет введены правильные координаты
    0 - для выхода из цикла
    :return: координаты str ('a1' / 'h7') или None
    """
    while True:
        cord: str = input('введите шахматную координату: ').strip()
        if cord == '0':
            return
        if len(cord) != 2:
            print("Количество введенных символлов должно быть 2")
            continue

        x, y = cord[0].lower(), cord[1]
        if x not in X_LST or not y.isdecimal() or y not in Y_LST:
            print("не верная координата. Повторите ввод.")
            continue

        return x + y


def get_cord_clr(cord: str) -> str:
    """
    Функция возвращает цвет поля переданный координаты
    :param cord: string, from input_cord()
    :return: 'black' or 'white'
    """
    x, y, *z = cord
    x = X_LST.index(x)
    y = Y_LST.index(y)
    return CLR[(x + y) % 2]


while True:
    cord1, cord2 = input_cord(), input_cord()

    if cord1 and cord2:
        clr1, clr2 = map(get_cord_clr, [cord1, cord2])
        sfx = '' if clr1 == clr2 else 'не'
        print(f"Цвета координат {cord1}({clr1}) и {cord2}({clr2}) {sfx} совпадают")

        if input("Хотите повторить? (y/n): ").strip()[0].lower() != 'y':
            break
    else:
        if input("Выйти? (y/n): ").strip()[0].lower() == 'y':
            break
