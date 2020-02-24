#1. Напишите функцию (F): на вход список имен и целое число N; на выходе список длины N случайных имен из первого списка
# (могут повторяться, можно взять значения: количество имен 20, N = 100, рекомендуется использовать функцию random);
from functools import reduce


def list_name_generator (list_name, n):
    import random
    list_name_generated = []
    for i in range (n+1):
        list_name_generated.append(random.choice(list_name))
    return list_name_generated

#2. Напишите функцию вывода самого частого имени из списка на выходе функции F;
a = list_name_generator(['Ciri','Geralt', 'Ofir', 'Shani', 'Yennifer', 'Triss', 'Myshovur', 'Kagyr', 'Zoltan', 'Dondelion'], 100)
print(a)
def most_often_name (a):
    counter_repeat = {}
    for i in a:
        counter = counter_repeat.get(i, 0)
        counter_repeat[i] = counter + 1
    counter_repeat = list(counter_repeat.items())
    counter_repeat.sort(key=lambda kv: kv[1], reverse=True)
    return counter_repeat[:1]
print (most_often_name(a))

 #3. Напишите функцию вывода самой редкой буквы, с которого начинаются имена в списке на выходе функции F.

def most_rare_fitst_letter (a):
#Нахожу первую букву и определяю ее в отдельный лист
    first_letter_list = []
    first_letter_list = [i[0] for i in a]
#Считаю количество повторений и переношу в словарь
    dict_rare_letter = {a: first_letter_list.count(a) for a in first_letter_list}
    print(dict_rare_letter) #Cловарь

# Создаю список значений
    letter_values = []
    for values in dict_rare_letter.values():
        letter_values.append(values)
# Создаю список из ключей которым соответвует минимальное значение
    rare_letter_list = []
    for items, values in dict_rare_letter.items():
        if values == min(letter_values): #Хотелось сделать без min, но тогда добавлялся только один value
            rare_letter_list.append(items)
    return rare_letter_list
print('Самая редкая первая буква:', most_rare_fitst_letter(a))
print()

#4.  В файле с логами найти дату самого позднего лога (по метке времени):
import datetime
import functools
with open('log', mode = 'rt', encoding = 'utf-8') as log_file:
    text = log_file.read().splitlines()
all_data = list(map(lambda x: datetime.datetime.strptime(x.split(" - ")[0], '%Y-%m-%d %H:%M:%S,%f'), text))
latest_date = functools.reduce(lambda x, y: x if y < x else y, all_data)
print ('Краянее время записи в лог:', latest_date)




