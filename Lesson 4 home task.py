# LIGHT:
#
# 1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);

import random

name = ('маша','паша','женя','леша','кирилл','вика','марина','дима','сергей','антон','борис','саша','вика','олег','даша','наташа','вова','аркадий','святослав')

def name_list(name, n=100):
    return random.choices(name, k=n)
print(name_list(name))


# 2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
max_list = max(name_list(name))
print(max_list)

# 3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.
min_ward = name_list(name)
latter = list(map(lambda x: x[0], min_ward))
min_latter=min(latter)
print(min_latter)


# PRO:
#
# LIGHT +
#
# 4.  В файле с логами найти дату самого позднего лога (по метке времени): https://drive.google.com/open?id=1pKGu-u2Vvtx4xK8i2ZhOzE5rBXyO4qd8
