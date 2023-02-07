import aritméticas2
import agregar_archivo

def correr():
   while True:
        opcion= input("\t+) Suma\n\t-) Resta\n\t*) Multiplicación\n\t//) División\n\t!) Factorial\n\t^) Potencia\n\t~) Salir\nIngrese una opción: ")
        #ejecuta la suma
        if opcion== "+":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            lista_suma= []
            num_suma= int(input("Digite el numero por sumar (0 para terminar): "))
            while num_suma !=0:
                lista_suma.append(num_suma)
                num_suma= int(input("Digite el numero por sumar (0 para terminar): "))
            suma= aritméticas2.calcular_suma(lista_suma)
            print(f"El resultado de la suma es: {suma}")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(suma))  
        #ejecuta la resta
        elif opcion== "-":
            #guarda la operación en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            num_minuendo= int(input("Digite el minuendo de la resta: "))
            num_sustraendo= int(input("Digite el sustraendo de la resta: "))
            resta= aritméticas2.calcular_resta(num_minuendo, num_sustraendo)
            print(f"El resultado de la resta es: {resta} ")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(resta))  
        #ejecuta la multiplicación
        elif opcion== "*":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            lista_multiply= []
            num_multiply= int(input("Digite el numero por multiplicar (0 para terminar): "))
            while num_multiply !=0:
                lista_multiply.append(num_multiply)
                num_multiply= int(input("Digite el numero por multiplicar (0 para terminar): "))
            multiplicacion= aritméticas2.calcular_multiplicar(lista_multiply)
            print(f"El resultado de la multiplicación es: {multiplicacion}")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(multiplicacion))
        #ejecuta la división
        elif opcion== "//":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            num_dividendo= int(input("Digite el dividendo de la división: "))
            num_divisor= int(input("Digite el divisor de la divsión: "))
            division= aritméticas2.calcular_division(num_dividendo, num_divisor)
            print(f"El resultado de la división es: {division}") #imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(division))
        #ejecuta el factorial
        elif opcion== "!":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide el numero al usuario
            num_factorial= int(input("Calcular el factorial de: "))
            if num_factorial<0:
                print("Error, el numero debe ser entero positivo")
            else:
                factorial= aritméticas2.calcular_factorial(num_factorial)
                print(f"El factorial es: {factorial}")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(factorial))
        #ejecuta la potencia
        elif opcion== "^":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            num_base= int(input("Digite la base de la potencia: "))
            num_exponente= int(input("Digite el exponente de la potencia: "))
            potencia= aritméticas2.calcular_potencia(num_base, num_exponente)
            print(f"La potencia es: {potencia}")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(potencia))
        #salir
        elif opcion== "~":
            break
        else:
            print("Error, opción invalida, intente de nuevo")
        print()
correr()