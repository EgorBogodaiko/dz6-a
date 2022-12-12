# 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]


from random import randint as rnd
def randomize(input_list, qtys):
    """Функция для создания массива со случайными целыми числами из пустого входящего массива.
    На входе ожидается пустой массив и количество элементов, которое должно быть сгенерировано
    """
    input_list = [rnd(0,10) for x in range(qtys)]
    return input_list
    
def mult_elem (input_list):
    """Функция возвращает массив из значений, где каждое значение = входящиймассив[индекс]*входящиймассив[размер массива - индекс]
    На входе ожидает массив"""
    multiplied_list = []
    for position,elem in enumerate(input_list[0:len(input_list)//2]):
        multiplied_list.append(elem*input_list[len(input_list)-position-1])
    return multiplied_list

qty = input('Введите количество элементов массива: ')
pure_list = []
pure_list = randomize(pure_list,int(qty))
print(pure_list)
print("Умноженные элементы: ",(mult_elem(pure_list)))