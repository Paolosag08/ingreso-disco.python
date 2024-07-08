# 1. Solicitar al usuario que ingrese la edad del cliente

edad = int(input('Ingrese la edad del cliente: '))
permitido = False

# 2. Verifico si la edad ingresada cumple con los requisitos

if edad >= 18:
    permitido = True
else:
    permitido = False

# 3. Muestro al usuario si su cliente puede o no ingresar a la disco

if permitido:
    print('El cliente puede entrar a la disco')
else:
    print('El cliente no puede entrar por ser menor de edad.')