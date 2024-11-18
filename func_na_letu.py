from os import write

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x,y: x == y, first , second))
print(list(result))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'a',encoding='utf-8') as file:
            for i in range(len(data_set)):
                file.write(str(data_set[i]) + "\n")
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

with open('example.txt', 'r',encoding='utf-8') as file:
    print(file.read())

import random
class MysticBall:
    def __init__(self,word):
        self.word = word

    def __call__(self):
        return random.choice(self.word)

ball = MysticBall(["Да", "Нет", "Возможно", "Спросите еще раз"])
print(ball())
print(ball())
print(ball())
print(ball())
#Результатом должен быть список совпадения букв в той же позиции:
#[False, True, True, False, False, False, False, False, True, False, False, False, False, False]
#Где True - совпало, False - не совпало.

#Замыкание:#
#Напишите функцию get_advanced_writer(file_name), принимающую название файла
# для записи.
#Внутри этой функции, напишите ещё одну - write_everything(*data_set),
# где *data_set - параметр принимающий неограниченное количество данных любого типа.
#Логика write_everything заключается в добавлении в файл file_name всех данных
# из data_set в том же виде.
#Функция get_advanced_writer возвращает функцию write_everything.

#Данный код:
#write = get_advanced_writer('example.txt')
#write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
#Запишет данные в файл в таком виде:

#Метод __call__:
#Создайте класс MysticBall, объекты которого обладают атрибутом words
# хранящий коллекцию строк.
#В# этом классе также определите метод __call__ который будет случайным
# образом выбирать слово из words и возвращать его. Для случайного выбора с
# одинаковой вероятностью для каждого данного в коллекции можете использовать
# функцию choice из модуля random.

#Ваш код (количество слов для случайного выбора может быть другое):
#from random import choice
## Ваш класс здесь
#first_ball = MysticBall('Да', 'Нет', 'Наверное')
#print(first_ball())
#print(first_ball())
#print(first_ball())
#Примерный результат (может отличаться из-за случайности выбора):
#Да
#Да
#Наверное#