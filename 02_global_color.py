# -*- coding: utf-8 -*-
# painting library
import simple_draw as sd

sd.set_screen_size(1500, 850)
#first point needed to start drawing
first_point = sd.get_point(150, 150)
# defining var for some colors
red = sd.COLOR_RED
orange = sd.COLOR_ORANGE
yellow = sd.COLOR_YELLOW
green = sd.COLOR_GREEN
cyan = sd.COLOR_CYAN
blue = sd.COLOR_BLUE
purple = sd.COLOR_PURPLE

#creating dictionary for all colors
color_dict = {
    1: red,
    2: orange,
    3: yellow,
    4: green,
    5: cyan,
    6: blue,
    7: purple
}

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
# вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом
# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

#function for drawing, which uses info about count of angles, angle width, start coordinates, length of line(vector)
#and it's color
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

#function for asking user about color. every iteration for new figure changing start point
def all_figures(start_point, angle, length):
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
    distance = 150
    for iterations in range(3, 11):
        drawing(iterations=iterations, angle=angle, start_point=start_point, length=length, color=asked_color)
        distance += 80
        start_point = sd.get_point(distance, 150)


all_figures(start_point=first_point, angle=0, length=20)
sd.pause()
