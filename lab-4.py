"""# 1
string = "Hello, World!"

# 1.1.
length = len(string)
print(f"Длина строки: {length}")

# 1.2.
lowercase = string.lower()
print(f"Lowercase: {lowercase}")

# 1.3.
uppercase = string.upper()
print(f"Uppercase: {uppercase}")

# 1.4.
replaced = string.replace("Hello", "Hi")
print(f"Замена: {replaced}")

# 1.5.
split_string = string.split(",")
print(f"Split string: {split_string}")

# 1.6.
starts_with = string.startswith("Hello")
print(f"Строка начинается со слова 'Hello': {starts_with}")

# 1.7.
ends_with = string.endswith("World!")
print(f"Строка заканчивается на 'World!': {ends_with}")

# 1.8.
index = string.find("World")
print(f"Индекс начала слова 'World': {index}")

# 1.9.
is_alphanumeric = string.isalnum()
print(f"Строка содержит только буквы и цифры?: {is_alphanumeric}")

# 1.10. Strip whitespace characters
stripped = string.strip('!')
print(f"Stripped string: {stripped}")"""


# 2

"""students = []

while True:
    student = input(
        "Введите имя и класс ученика (или нажмите «q», чтобы выйти):")
    if student == 'q':
        break
    students.append(student)


students.sort(key=lambda x: int(x.split()[-1]))

for student in students:
    name, grade = student.split()
    print(f"{name} ({grade})")
"""

"""# 3.1

string = input("Введите строку: ")

upper_count = 0
lower_count = 0
for char in string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1


if upper_count > lower_count:
    print(string.upper())
else:
    print(string.lower())
"""

# 3.2

while True:
    num1 = input("Введите первое число: ")
    if num1.isdigit():
        num1 = int(num1)
        break
    else:
        print("Неправильно, необходимо ввести число")

while True:
    num2 = input("Введите второе число: ")
    if num2.isdigit():
        num2 = int(num2)
        break
    else:
        print("Неправильно, необходимо ввести число")

print(num1, "+", num2, "=", num1 + num2)
