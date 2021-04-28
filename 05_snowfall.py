# -*- coding: utf-8 -*-
from pprint import pprint
from random import randint

import simple_draw as sd

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
sd.set_screen_size(650, 450)

coordinate_x = {(n + 1) * 30 for n in range(N)}
print(coordinate_x)
snow_form = {}
for x in coordinate_x:
    factor_a = randint(4, 8) / 10
    factor_b = randint(25, 45) / 100
    factor_c = randint(50, 70)
    change_y = 0
    y = 400
    z = 0
    coord_x = x
    snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x


def snowfall(size):
    y = 600
    while y >= 40:
        if sd.user_want_exit():
            break
        for x in snow_form:
            factor_a = snow_form[x][0]
            factor_b = snow_form[x][1]
            factor_c = snow_form[x][2]
            change_y = snow_form[x][3]
            y = snow_form[x][4] - randint(1, 3)
            z = randint(-3, 3)
            coord_x = snow_form[x][6] + z
            snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x
        for x in snow_form:
            factor_a = snow_form[x][0]
            factor_b = snow_form[x][1]
            factor_c = snow_form[x][2]
            change_y = snow_form[x][3]
            y = snow_form[x][4] - snow_form[x][3]
            z = snow_form[x][5]
            coord_x = snow_form[x][6]
            start_point = sd.get_point(coord_x, y)
            sd.snowflake(start_point, length=size, color=sd.COLOR_WHITE, factor_a=factor_a, factor_b=factor_b,
                         factor_c=factor_c)
            # sd.sleep(0.005)
            if y < 40:
                y = 600
                snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x
        if y >= 40:
            for x in snow_form:
                factor_a = snow_form[x][0]
                factor_b = snow_form[x][1]
                factor_c = snow_form[x][2]
                change_y = snow_form[x][3]
                y = snow_form[x][4] - snow_form[x][3]
                z = snow_form[x][5]
                coord_x = snow_form[x][6]
                start_point = sd.get_point(coord_x, y)
                sd.snowflake(start_point, length=size, color=sd.background_color, factor_a=factor_a, factor_b=factor_b,
                             factor_c=factor_c)
                snow_form[x] = factor_a, factor_b, factor_c, change_y, y, z, coord_x


snowfall(randint(20, 40))

# while True:
#     sd.clear_screen()
#     pass
#     pass
#     pass
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg
