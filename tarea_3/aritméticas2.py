#calcula la división entera de dos numeros
def calcular_division(num_1, num_2):
    return num_1 // num_2

#calcula el factorial de un numero
def calcular_factorial(n):
    if n==0:
        return 1
    else:
        return n *calcular_factorial(n-1)

#calcula la potencia de un numero
def calcular_potencia(base, exponente):
    return base ** exponente

# calcula la suma
def calcular_suma (number_list):
    suma = 0
    for num in number_list:
        suma =  suma + num
    return suma

# Definir Multiplicacion
def calcular_multiplicar(number_list):
    producto = 1
    for num in number_list:
        producto *= num
    return producto

# Definir Resta  
def calcular_resta( num_1, num_2):
    return num_1 - num_2