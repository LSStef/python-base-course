name = ['МАША','ДАША','НАТАША','кирилл','аЛЕКСЕЙ','Нина']
name_lenght = list(map(len,name))
print(name_lenght)

from _functools import reduce
# name_reduce = reduce(len,name)
# print(name_reduce)

list_temp = [43, 12, 41, 100, 101, 4]
list_tem_ = [43, 12, 41, 102, 101, 4]
max = reduce(lambda a, b: a if a > b else b, list_temp)
#max1 = list(map(lambda a, b: a if a > b else b, list_temp))
print(max)
#print(max1)

#filter
list_50 = list(filter(lambda x: x>50, list_temp))
list_50_1 = list(filter(lambda x: x>50, list_tem_))
print(list_50)
print(list_50_1)

#sorted
list_temp_sort = sorted(list_temp, reverse = True) # параметр реверс сортировка в обратном порядке
print(list_temp_sort)

# key сортировка по ключам

name_sort = sorted(name)
print(name_sort)
#сортировка по 2 букве

list_name_sort_key = sorted (name, key = lambda x: x[1])
print(list_name_sort_key)

# напишем какую нибудь для поиска суммы элементов в списке, мы делаем так:
my_list = (10, 20, 30)
def find_sum(my_list):  # объявляем функцию, даем ей имя, и в скобках указываем что она принимает,
    # то есть какие данные будут даваться ей в обработку, с которыми она будет делать какие-то операции, которые мы пропишем в теле функции
    sum_m = 0  # дальше идет тело функции через отступ
    for i in my_list:
        sum_m += i
    return sum_m  #здесь вместо print делаем return, чтобы когда мы в дальнейшем обращались к этой функции,
    # она не просто выводила на печать полученный результат, а возвращала его, то есть его можно будет присвоить к какой то переменной и т.п
ab = find_sum(my_list)
print(ab)

