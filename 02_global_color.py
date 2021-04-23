# -*- coding: utf-8 -*-
import simple_draw as sd

sd.set_screen_size(1500, 850)

first_point = sd.get_point(150, 150)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg


def drawing(iterations, angle, start_point, length):
    into_start_point = start_point
    for _ in range(iterations-1):
        every_angle = int(360 / iterations)
        vector = sd.get_vector(start_point=into_start_point, angle=angle, length=length, width=1)
        vector.draw()
        into_start_point = vector.end_point
        angle += every_angle
        sd.sleep(0.1)
    sd.line(start_point=into_start_point, end_point=start_point, color=sd.COLOR_YELLOW, width=1)


def all_figures(start_point, angle, length):
    distance = 150
    for iterations in range(3, 11):
        drawing(iterations=iterations, angle=angle, start_point=start_point, length=length)
        distance += 80
        start_point = sd.get_point(distance, 150)


# def triangle(start_point, angle, length):
#     drawing(iterations=3, angle=angle, start_point=start_point, length=length)
#
#
# def square(start_point, angle, length):
#     drawing(iterations=4, angle=angle, start_point=start_point, length=length)
#
#
# def pentagon(start_point, angle, length):
#     drawing(iterations=5, angle=angle, start_point=start_point, length=length)
#
#
# def hexagon(start_point, angle, length):
#     drawing(iterations=6, angle=angle, start_point=start_point, length=length)
#
#
# def heptagon(start_point, angle, length):
#     drawing(iterations=7, angle=angle, start_point=start_point, length=length)
#
#
# def octagon(start_point, angle, length):
#     drawing(iterations=8, angle=angle, start_point=start_point, length=length)
#
#
# def decagon(start_point, angle, length):
#     drawing(iterations=10, angle=angle, start_point=start_point, length=length)


all_figures(start_point=first_point, angle=0, length=20)
sd.pause()
