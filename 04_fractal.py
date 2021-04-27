# -*- coding: utf-8 -*-
from random import randint
import simple_draw as sd
first_point = sd.get_point(750, 150)
sd.set_screen_size(1800, 1000)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов:
def draw_branches(start_point, start_angle, start_length, width):
    # two branches, left and right
    branch_1 = sd.get_vector(start_point=start_point, angle=start_angle + 30, length=start_length, width=width)
    branch_1.draw()
    branch_2 = sd.get_vector(start_point=start_point, angle=start_angle - 30, length=start_length, width=width)
    branch_2.draw()
    # target 2, after first two branches changing length, angle, width and start point of drawing
    start_length *= (0.75 + (randint(-15, 15) / 100))
    start_point = branch_1.end_point
    start_angle = branch_1.angle + randint(-12, 12)
    width = width - 1
    if start_length > 10:
        # continuing of left root, recursion
        draw_branches(start_point=start_point, start_angle=start_angle, start_length=start_length, width=width)
    start_point = branch_2.end_point
    rand_int = randint(-12, 12)
    start_angle = branch_2.angle - rand_int
    if start_length > 10:
        # continuing of right root, recursion
        draw_branches(start_point=start_point, start_angle=start_angle, start_length=start_length, width=width)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
# root_point = get_point(300, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg
# можно поиграть -шрифтами- цветами и углами отклонения

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# first line, vertical part of tree
sd.line(sd.get_point(750, 0), sd.get_point(750, 150), width=14)
draw_branches(start_point=first_point, start_angle=90, start_length=175, width=12)

sd.pause()
