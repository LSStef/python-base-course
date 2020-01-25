# pip install pymorhy2
# pip install pymorhy2-dict
# pip install DAWG-Python

# import (C:\Users\stef2\Downloads\text.txt)

# 1) методами строк очистить текст от знаков препинания;
from pymorphy2 import MorphAnalyzer

htext='Все смешалось в доме Облонских. Жена узнала, что муж был в связи с бывшею в их доме француженкою-гувернанткой, и объявила мужу, что не может жить с ним в одном доме. Положение это продолжалось уже третий день и мучительно чувствовалось и самими супругами, и всеми членами семьи, и домочадцами. Все члены семьи и домочадцы чувствовали, что нет смысла в их сожительстве и что на каждом постоялом дворе случайно сошедшиеся люди более связаны между собой, чем они, члены семьи и домочадцы Облонских. Жена не выходила из своих комнат, мужа третий день не было дома. Дети бегали по всему дому, как потерянные; англичанка поссорилась с экономкой и написала записку приятельнице, прося приискать ей новое место; повар ушел вчера со двора, во время самого обеда; черная кухарка и кучер просили расчета'

'''
почему не работает? 
задаю список в списке все знаки и далее заменить . ошибка синтаксиса
a = [",", "."]
print(htext.replace("a"," "))
'''
clear_text = htext.replace("."," ").replace(","," ").replace("-","  ")
print(clear_text)



# 2) сформировать list со словами (split);

#list_str = list(htext)
#print(list_str)
#print(len(list_str))

'''
не получилось . по эксперементу я так понял это только для чисел?

intenger_list = [htext]
for intenger_list in htext:
    intenger_list.append(split)
print(intenger_list)
'''
list_split = clear_text.split()
print(list_split)
# это правильно ? или нужно list_split или что бы при выводе добовлялось слово споит?

# 3) привести все слова к нижнему регистру (map);
#print(htext.lower()) - зачем через мар и так раотает
#print(htext.upper())

intenger_list = [htext]
lower_htext = list(map(lambda x: x.lower(),intenger_list))
# не понял зачем через лист все это делать почему сразу map не рабботает?
# почему htext работает а list_split нет ?
print(lower_htext)

# 5) выполнить light с условием: в пункте 2 дополнительно к приведению к нижнему регистру выполнить лемматизацию.
# я вот тут искал метод или  фйнкцию light  и ошибка в номере занадния задание 3 дожно быть

import pymorphy2
morf_split = htext.lower().split()
print('задание про', morf_split)
morph = pymorphy2.MorphAnalyzer(morf_split)
print(morph)
# ошибка МTraceback (most recent call last): не знаю что значит даже по русски  видимо переменная морф не правильная
# 3) получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;



dict_temp = {}
for i in range(len(list_split)):
    dict_temp[list_split[i]] = list_split.count(list_split[i])
print(dict_temp)

# с этим как то не разобрался по теме. нужно еще пояснение


# 4) вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set).

'''
my_set_1 = set([unique])
my_set_2 = set(htext.split())
my_set_3=my_set_2.difference(my_set_1)
print(my_set_3)
'''
dict_ = {}
for word in list_split:
    dict_[word] = list_split.count(word)
dict_tolist = list(dict_.items())
# print(dict_tolist) # колличество повторений слов
dict_tolist.sort(key=lambda i: i[1], reverse = True)
top_five = dict_tolist[0:5]
print(top_five) #Пять самых частых слов



#вывести количество разных слов в тексте (set)

unique=len(set(htext.split()))
print(unique)




