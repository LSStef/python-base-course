import os  # импорт всего модуля

from os import mkdir  # импортирования отдельных функций
from os import mkdir as remover # не работает
from os import* # импортируется модуль целиком


# remover('test1')
# mkdir('test1')
# remover('test1')


print(getcwd())
print(list(walk(getcwd())))