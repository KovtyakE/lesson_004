# -*- coding: utf-8 -*-

# painting library
import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
# вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

sd.set_screen_size(1500, 850)
# first point needed to start drawing:
first_point = sd.get_point(650, 325)
# creating dictionary for all colors:
color_dict = {
    1: sd.COLOR_RED,
    2: sd.COLOR_ORANGE,
    3: sd.COLOR_YELLOW,
    4: sd.COLOR_GREEN,
    5: sd.COLOR_CYAN,
    6: sd.COLOR_BLUE,
    7: sd.COLOR_PURPLE
}
# creating dictionary for all figures, 3,4,5 etc is means count of iterations(angles):
figure_dict = {
    1: 3,
    2: 4,
    3: 5,
    4: 6,
    5: 7,
    6: 8,
    7: 9,
    8: 10
}
# for asking user about color
asked_color = 0
while asked_color == 0:
    try:
        ask_from_user = int(input("Выберите цвет фигур: \n1-Красный\n2-Оранжевый\n3-Желтый\n4-Зеленый\n"
                                  "5-Голубой\n6-Синий\n7-Фиолетовый:\n"))
    except:
        print("Вы ввели неверное значение, введите число от 1 до 7")
    else:
        if ask_from_user in range(1, 7):
            asked_color = color_dict[ask_from_user]
        else:
            print("Вы ввели неверное значение, введите число от 1 до 7")
# for asking user about figure
asked_figure = 0
while asked_figure == 0:
    try:
        ask_from_user = int(input("Выберите цвет фигур: \n1-Треугольник\n2-Квадрат\n3-Пятиугольник\n4-Шестиугольник\n"
                                  "5-Семиугольник\n6-Восьмиугольник\n7-Девятиугольник\n8-Десятиугольник:\n"))
    except:
        print("Вы ввели неверное значение, введите число от 1 до 8")
    else:
        if ask_from_user in range(1, 8):
            asked_figure = figure_dict[ask_from_user]
        else:
            print("Вы ввели неверное значение, введите число от 1 до 8")


# function for drawing, which uses info about (count of angles, angle width, start coordinates, length of line(vector)
# and it's color)
def drawing(iterations, angle, start_point, length, color):
    into_start_point = start_point
    # new var for cycle changing, iterations -1 because last line we drawing with two points
    for _ in range(iterations - 1):
        every_angle = int(360 / iterations)
        vector = sd.get_vector(start_point=into_start_point, angle=angle, length=length, width=1)
        vector.draw(color=color)
        into_start_point = vector.end_point
        angle += every_angle
        sd.sleep(0.1)
    sd.line(start_point=into_start_point, end_point=start_point, color=color, width=1)


# function every iteration for new figure changing start point
def all_figures(start_point, angle, length):
    # iterations means count of angles
    drawing(iterations=asked_figure, angle=angle, start_point=start_point, length=length, color=asked_color)


all_figures(start_point=first_point, angle=0, length=200)
sd.pause()
