# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# определитель усталости
# Ваш код дальше:
a = float(input('по шкале от 0 до 10, напишите, насколько Вы устали: '))
if a < 0.7:
    print('Кажется, Вы совсем не устали')
elif 0.7 <= a <= 4.8:
    print('Вы немного устали')
elif 4.9 <= a <= 7.5:
    print('Вы конкретно устали!')
elif 7.6 <= a <= 10:
    print('Вы чертовски устали!')
elif 10.1 <= a <= 20:
    print('Вам стоит полежать и поничегонеделать несколько дней')
elif a > 25:
    print('Вы приближаетесь к выгоранию')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
