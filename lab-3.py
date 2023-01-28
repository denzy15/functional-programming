import random
# 1
"""  
times = [3, 4, 8, 5]

counter = 0

while (counter < len(times)):
    tempArr = []
    for num in range(times[counter]):
        tempArr.append(num + 1)

    print(str(counter + 1) + '. iteration:')
    print(''.join(str(n) for n in tempArr))
    counter += 1
"""

# 2

"""my_list = [1, "hello", 3.14, [1, 2, 3], 333, 'PYTHON']
listRange = range(4)

for i in listRange:
    print(my_list[i])
"""

# 3

"""listRange2 = random.randint(1, 25)
templist = []

for i in range(random.randint(1, 25)):
    templist.append(random.random() * 100)
    templist.append(random.randrange(1, 100))

for item in enumerate(templist):
    print(item)
"""
# 4.1

"""print('Введите А:')
a = int(input())
print('Введите B:')
b = int(input())

print('=======')

if (a <= b):
    for i in range(a, b+1):
        print(i)
else:
    print('Число А должно быть <= B')"""

# 4.2
"""
print('Введите А:')
a = int(input())
print('Введите B:')
b = int(input())

print('=======')

if (a < b):
    for i in range(a, b+1):
        print(i)
else:
    for i in range(a, b-1, -1):
        print(i)
"""

# 4.3

"""print('Введите А:')
a = int(input())
print('Введите B:')
b = int(input())

print('=======')

start = a-1 if a % 2 == 0 else a
for i in range(start, b-1, -2):
    print(i)
"""

# 4.4


"""n = 8

current_cards = ""
loose_random_card = random.randint(1, n)

for i in range(n):
    if (i+1 != loose_random_card):
        current_cards += str(i+1)

print(loose_random_card)
print("===")

for i in range(1, 8 + 1):
    if (str(i) not in current_cards):
        print("Lost card = " + str(i))
"""
