#name = "Как тебя зовут Ваня Сидоров"

# print(name[15:19])
# print(name[20:])
# print(name[::-1])

# print(len(name))
# print(name.lower())
# print(name.upper())
# print(name.title())
# print(name.capitalize())

# pythonworld.ru - посмотри сайт про строки
# https://pythonworld.ru/tipy-dannyx-v-python/stroki-funkcii-i-metody-strok.html

# print(name.find('Ваня'))
#
#
# name = 'Иван'
# surname = 'Петров'
# money = 100

#wellcome = 'Привет, %s %s у вас на счете %i денег.' % (name, surname, money)
#wellcome = 'Привет, {} {} у вас на счете {} денег.'.format(name, surname, money)
#wellcome = F'Привет, {name} {surname} у вас на счете {money} денег.' (not support now)


#print(wellcome)


names = ['Ivan', 'Alisa', 'Bob', 'Qwerty']
# print(names[2])
# print(names[1:])
# print(names[1:3])
# print(names[::-1])

# names.append('olga')
# print(names)
#
# names.insert(0, 'Nikolay')
# print(names)
#
# names.remove('Ivan')
# print(names)
#
# names.append(1000)
# print(names)
#
# names.append('Bob')
# print(names)
# print(names.count('Bob'))
#
# names.pop()
# remove = names.pop(1)
# print(remove, " был удален")
# print(names)
#
#
# print("olga" in names)
#
#
# # кортеж это неизменяемый список (эконопит пямать)
# names = ("Ivan", "Alisa", 'Bob')


names = ['Ivan', 'Alisa', 'Bob', 'Qwerty']
# for name in names:
#     print(name)
#
# for sym in 'qwerty':
#     print(sym)
#


# выводить по строчно до 10 раз
# for number in range(10):
#     print(number, end='_')


# словари
# https://pythonworld.ru/tipy-dannyx-v-python/slovari-dict-funkcii-i-metody-slovarej.html

human = {"name": 'Ivan', 'surname': "Ivanov", 'age': '20', 'money': '100.10'}
# print('Привет %s %s, у вас на счете %i .' % (human['name'], human['surname'], human[money]))


# for key in human.keys():
#     print(key)

for key, value in human.items():
    print(key, "->", value)



# множества - это всегда уникальный набор данных

# names = {'Ivan', 'Olga', 'Ivan', "Bob"}
# numbers = {1, 2, 3, 4, 3, 4}
numbers = set([1, 2, 3, 4, 3, 43]) #функция set делает из кортежа множество с уникальными значениями
print(names)
print(numbers)
