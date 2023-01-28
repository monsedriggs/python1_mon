from math import factorial

#Pide el numero al usuario
num=int(input("Ingrese un numero entero positivo: \n"))

#Formula para calcular el factorial de un numero n!= n* (n-1)!
if num==0:
    #Si el numero ingresado es cero
    print(f"El factorial de {num} es: 1")
elif num<0:
    #Si el numero ingresado es negativo, mensaje de error
    print(f"Error, el numero debe ser positivo")
else:
    factorial_num= num *factorial((num-1))
    print(f"El factorial de {num} es: {factorial_num}")