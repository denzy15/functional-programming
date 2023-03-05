# 1

"""my_dict = {'name': 'Daniil', 'last_name': 'Mirshanov',
           'course': 3, 'specialization': 'computer science'}

# 1.1
print(f'Длина {len(my_dict)}')
# 1.2
print(f'Ключи словаря {my_dict.keys()}')
# 1.3
print(f'Значения словаря {my_dict.values()}')
# 1.4

print(f'Пара ключ-значение словаря {my_dict.items()}')
# 1.5

my_dict.update({'age': 20, 'course': 4})
print(f'Обновленный словарь {my_dict}')

# 1.6
print(my_dict.get('name'))
print(my_dict.get('course'))
print(my_dict.get('d'))"""

# 2.1

"""country_rivers_dict = {'Mississippi': 'USA', 'Fraser': 'Canada',
                       'Rio Grande': 'Mexico',  'Ili': 'Kazakhstan', 'Volga': 'Russia'}

rivers = ['Huanghe', 'Volga', 'Amur', 'Fraser',
          'Mississippi', 'Ili', 'Lena', 'Rio Grande']


for river in rivers:
    if river in country_rivers_dict.keys():
        print(f'{river} находится в {country_rivers_dict[river]}')
    else:
        print(f'Река {river} не найдена')

"""

# 2.2

"""comments = {}

while True:
    line = input().strip()
    if not line or not ':' in line:
        break
    line = line.split(':')
    name = line[0]
    comment = line[1]
    comments.update({name: comment})

unique = set(comments.keys())
print(f'Уникальных пользователей: {len(unique)}')
"""

# 2.3

"""
phones = {}

n = int(input('Введите N'))

for i in range(n):
    phone = input('Имя и телефон:')
    name = phone.split()[0]
    number = phone.split()[1]
    phones.update({name: number})

input_name = input('Поиск по имени: ')

if input_name in phones.keys():
    print(phones.get(input_name))
else:
    print('Нет в телефонной книге')
"""
# 2.4

"""vacations = {}

n = int(input('Введите N: '))

for i in range(n):
    phone = input('Имя, день и месяц: ')
    name = phone.split()[0]
    month = phone.split()[2]
    vacations.update({name: month})

input_month = input('Месяц отпуска: ')


names = []

for key, value in vacations.items():
    if value == input_month:
        names.append(key)


print(' '.join(names))
"""
