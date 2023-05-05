first_number = input('Ingresa un numero: ')
secound_number = input('Ingresa otro numero: ')

if int(first_number) > int(secound_number):
    print('El primer numero es mayor')
    print('Los numeros no son iguales')
    print('El segundo numero no es mayor')
elif int(first_number) == int(secound_number):
    print('Los numeros son iguales')
    print('El primer numero no es mayor')
    print('El segundo numero no es mayor')
elif int(first_number) < int(secound_number):
    print('El segundo numero es mayor')
    print('Los numeros no son iguales')
    print('El primer numero no es mayor')


print()

my_animal = 'Leon'
your_animal = input('Cual es tu animal favorito? ')

if your_animal.capitalize() == my_animal.capitalize():
    print('Ese es mi animal favorito tambien')
else:
    print('Ese no es mi animal favorito')