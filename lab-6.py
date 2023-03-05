import random
# 1
"""
my_tuple = (1, 4, 2, 3, 5)

# 1. len()
print(len(my_tuple))

# 2. sorted()
print(sorted(my_tuple))

# 3. max()
print(max(my_tuple))

# 4. min()
print(min(my_tuple))

# 5. tuple()
my_list = [1, 2, 3]
my_new_tuple = tuple(my_list)
print(my_new_tuple)

# =======================================

set_1 = {'Daniil', 'Mirshanov', 20,
         'Satbayev University', 'Computer Science'}
set_2 = {'Python', 'JavaScript', 'Java'}

# 1.
print(len(set_1))

# 2.
set_1.add('Hello')
print(set_1)

# 3.
set_1.remove('Hello')
print(set_1)

# 4.
set_3 = set_1.union(set_2)
print(set_3)

# 5.
set_1.clear()


"""


# 1


"""def fill_tuple(start, end, count):
    return tuple(random.randint(start, end) for _ in range(count))


tuple_1 = fill_tuple(0, 5, 10)
print(f"Tuple 1: {tuple_1}")

tuple_2 = fill_tuple(-5, 0, 10)
print(f"Tuple 2: {tuple_2}")

tuple_3 = tuple_1 + tuple_2
print(f"Tuple 3: {tuple_3}")

# Count the number of zeros in the third tuple
count_zeros = tuple_3.count(0)
print(f"Количество нулей в tuple_3: {count_zeros}")

"""
# 2

"""my_tuple = (1, (42, (3.14, ((3+2j), ('Конечная строка', ())))))

new_tuple = my_tuple[1][1][1][1][0]

print(new_tuple)"""


# 3

"""categories = ["Travel", "Lunch", "Dinner", "Entertainment"]

expenses = [[0 for j in range(len(categories))] for i in range(7)]

# Prompt the user to enter their expenses for each day of the week
for i in range(7):
    for j in range(len(categories)):
        expense = float('{:.2f}'.format(random.random() * 100))
        expenses[i][j] = expense

# Calculate the total weekly spending
total = 0
for i in range(7):
    daily_total = float('{:.2f}'.format(sum(expenses[i])))
    print("Траты за день", i+1, ":", daily_total)
    total += daily_total

print("Total expenses for the week:", total)

print(expenses)"""


# 4

"""student_names = input("Введитее имена: ").split()

student_tuple = tuple(student_names)

print("Имена содержащие `ва`:")
for name in student_tuple:
    if "ва" in name.lower():
        print(name)
"""

# 5

# Жаз көңіл жарқылдаған бұл бір шағым


letters = {
    'а': 'a', 'ә': 'á', 'б': 'b', 'в': 'v', 'г': 'g', 'ғ': 'ǵ', 'д': 'd', 'е': 'e', 'ё': 'io', 'ж': 'j', 'з': 'z',
    'и': 'i', 'й': 'ı', 'к': 'k', 'қ': 'q', 'л': 'l', 'м': 'm', 'н': 'n', 'ң': 'ń', 'о': 'o', 'ө': 'ó', 'п': 'p',
    'р': 'r', 'с': 's', 'т': 't', 'у': 'ý', 'ұ': 'u', 'ү': 'ú', 'ф': 'f', 'х': 'h', 'һ': 'h', 'ц': 'ts', 'ч': 'ch',
    'ш': 'sh', 'щ': 'sch', 'ъ': '', 'ы': 'y', 'і': 'i', 'ь': '', 'э': 'e', 'ю': 'iu', 'я': 'ia'
}

cyrillic_text = input("Введите казахский текст на кириллице: ")

latin_text = ''
for letter in cyrillic_text:
    latin_text += letters.get(letter.lower(), letter)


print(latin_text)

