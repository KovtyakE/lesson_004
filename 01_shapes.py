# -*- coding: utf-8 -*-

import simple_draw as sd

sd.set_screen_size(1200, 600)
# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# функция рисования линий с передачей данных о количестве углов, величине каждого угла, угле направления первого
# вектора, начальной точке и длине вектора
def drawing(iterations, every_angle, angle, start_point, length):
    for _ in range(iterations):
        line = sd.get_vector(start_point=start_point, angle=angle, length=length, width=1)
        line.draw()
        start_point = line.end_point
        angle += every_angle
        sd.sleep(0.1)


point_triangle = sd.get_point(150, 150)
def triangle(start_point, angle, length):
    for _ in range(24):
        angle += 15
        into_start_point = start_point
        for _ in range(3):
            line = sd.get_vector(start_point=into_start_point, angle=angle, length=length, width=1)
            line.draw()
            into_start_point = line.end_point
            angle += 120
        sd.sleep(0.01)
triangle(point_triangle, 0, 100)

point_square = sd.get_point(400, 150)
def square(start_point, angle, length):
    for _ in range(24):
        angle += 15
        into_start_point = start_point
        for _ in range(4):
            line = sd.get_vector(start_point=into_start_point, angle=angle, length=length, width=1)
            line.draw()
            into_start_point = line.end_point
            angle += 90
        sd.sleep(0.01)
square(point_square, 0, 100)

point_pentagon = sd.get_point(200, 420)
def pentagon(start_point, angle, length):
    for _ in range(12):
        angle += 30
        into_start_point = start_point
        for _ in range(5):
            line = sd.get_vector(start_point=into_start_point, angle=angle, length=length, width=1)
            line.draw()
            into_start_point = line.end_point
            angle += 72
        sd.sleep(0.01)
pentagon(point_pentagon, 0, 100)

point_hexagon = sd.get_point(800, 250)
def hexagon(start_point, angle, length):
    drawing(6, 60, angle, start_point, length)
hexagon(point_hexagon, 0, 100)

point_octagon = sd.get_point(1000,400)
def octagon(start_point, angle, length):
    drawing(8, 45, angle, start_point, length)
octagon(point_octagon, 0, 70)



# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
