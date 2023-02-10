import random
# 1
"""students = []


def sortByClass(e):
    return e.split()[1]


for i in range(5):
    print("Введите имя студента и его предмет ч/з пробел")
    std = input()
    students.append(std)

students.sort(key=sortByClass)

print('====================')
print('Сортированный список')

for i in range(5):
    print(students[i])

"""
# 2
"""
student_info = [
    {'name': 'Daniil', 'grades': ['3', '5', '7', '2']},
    {'name': 'Alex', 'grades': ['1', '1', '2', '2']},
    {'name': 'Oleg', 'grades': ['10', '8', '7', '9']},
    {'name': 'Yegor', 'grades': ['3', '5', '2', '2']},
]


name = input('Введите имя: ')

for i in range(len(student_info)):
    if name.lower() == student_info[i]['name'].lower():
        print('Оценки студента ' + name + ":")
        print(', '.join(student_info[i]['grades']))
        break

"""
# 3
"""numbers = []
while True:
    number = int(input("Введите число (0 чтобы остановиться): "))
    if number == 0:
        break
    numbers.append(number)

numbers.sort()

print("Введенные числа по возрастанию:")
for number in numbers:
    print(number)
"""

# 4
"""numbers = []
while True:
    number = int(input("Введите число (0 чтобы остановиться): "))
    if number == 0:
        break
    numbers.append(number)

numbers.sort(reverse=True)

print("Введенные числа по убыванию:")
for number in numbers:
    print(number)
"""


# 5
"""random_numbers = set()
while len(random_numbers) < 6:
    random_numbers.add(random.randint(1, 49))

random_numbers = list(random_numbers)
random_numbers.sort()

print("Номера для билета:", random_numbers)
"""


# 6

"""
def is_sorted(lst):
    if len(lst) < 2:
        return True
    order = None
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            if order == False:
                return False
            order = True
        elif lst[i] < lst[i - 1]:
            if order == True:
                return False
            order = False
    return True


input_list = []

for i in range(5):
    input_list.append(int(input('Введите число: ')))

print(is_sorted(input_list))
"""
