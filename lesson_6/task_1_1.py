"""
Задание 1.
Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы
На каждый скрипт нужно два решения - исходное и оптимизированное.
Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler
Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler
Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.
ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.
Это файл для первого скрипта
"""
from memory_profiler import memory_usage


def decor(func):
    def wrapper():
        m1 = memory_usage()
        res = func()
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper


# Исходное решение - задание 1_2 из курса 'Основы языка Python'
@decor
def func():
    # Создать список, состоящий из кубов нечётных чисел от 1 до 1000
    odd_numb_cube = []
    for idx in range(0, 1001):
        if idx % 2:
            odd_numb_cube.append(idx ** 3)
    print("Список, состоящий из кубов нечетных чисел от 1 до 1000:\n", odd_numb_cube)
    # Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
    sum_of_numbers = 0
    for numb in odd_numb_cube:
        member = numb
        sum_of_digits = 0
        while member:
            sum_of_digits += member % 10
            member //= 10
        if not sum_of_digits % 7:
            sum_of_numbers += numb
    print("Сумма чисел из списка, сумма цифр которых делится нацело на 7:", sum_of_numbers)
    # К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
    # списка, сумма цифр которых делится нацело на 7.
    sum_of_numbers = 0
    for numb in odd_numb_cube:
        numb += 17
        member = numb
        sum_of_digits = 0
        while member:
            sum_of_digits += member % 10
            member //= 10
        if not sum_of_digits % 7:
            sum_of_numbers += numb
    print("Сумма чисел из списка, сумма цифр которых делится нацело на 7, после добавления 17 "
          "к каждому элементу списка:", sum_of_numbers)


# Оптимизированное решение
@decor
def func2():
    # Создать список, состоящий из кубов нечётных чисел от 1 до 1000
    odd_numb_cube = [x ** 3 for x in filter(lambda x: x % 2, range(0, 1001))]
    # Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7
    sum_of_numbers = 0
    for numb in odd_numb_cube:
        member = numb
        sum_of_digits = 0
        while member:
            sum_of_digits += member % 10
            member //= 10
        del member
        if not sum_of_digits % 7:
            sum_of_numbers += numb
        del sum_of_digits
    # К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого
    # списка, сумма цифр которых делится нацело на 7.
    sum_of_numbers_2 = 0
    for numb in odd_numb_cube:
        numb += 17
        member = numb
        sum_of_digits = 0
        while member:
            sum_of_digits += member % 10
            member //= 10
        del member
        if not sum_of_digits % 7:
            sum_of_numbers_2 += numb
        del sum_of_digits
    return f"Список, состоящий из кубов нечетных чисел от 1 до 1000:\n {odd_numb_cube}\n" \
           f"Сумма чисел из списка, сумма цифр которых делится нацело на 7: {sum_of_numbers}\n" \
           f"Сумма чисел из списка, сумма цифр которых делится нацело на 7, после добавления 17 " \
           f"к каждому элементу списка: {sum_of_numbers_2}"


if __name__ == '__main__':
    print('Исходное решение')
    res1, mem_dif = func()
    print(f'Выполнение исходного решения заняло {mem_dif} Mib')  # 0.015625 Mib
    print('\nОптимизированное решение')
    res2, mem_dif = func2()
    print(res2)
    print(f'Выполнение оптимизированного решения заняло {mem_dif} Mib')  # 0.00390625 Mib

'''С целью оптимизации памяти для создания списка, состоящего из кубов нечётных чисел от 1 до 1000 вместо цикла 
был использован List Comprehensions. Также для возврата результата были использованы f-строки. Всё это привело
к оптимизации памяти'''