fullName = 'Daniil Mirshanov'
age = 20
subjects = ['Functional programming', 'Mobile apps development',
            'WEB development', 'Data analysis']

print('Сколько вам лет?')

# Ввод данных
inputAge = int(input())

if (inputAge == age):
    print('Вы мой ровестник')
elif (inputAge > age):
    print('Вы старше меня)')
else:
    print('Я старше вас на ' + str(age - inputAge) + ' лет')
