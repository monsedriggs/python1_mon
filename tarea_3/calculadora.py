import aritméticas2
import agregar_archivo

def correr():
   while True:
        opcion= input("\t+) Suma\n\t-) Resta\n\t*) Multiplicación\n\t/) División\n\t!) Factorial\n\t^) Potencia\n\t~) Salir\nIngrese una opción: ")
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
            #guarda los numeros en un archivo
            agregar_archivo.agregar_numeros(lista_suma)
            #invoca al método de suma
            suma= aritméticas2.calcular_suma(lista_suma)
            print(f"El resultado de la suma es: {suma}")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(suma))  
        #ejecuta la resta
        elif opcion== "-":
            #guarda la operación en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            lista_resta=[] #lista para guardar luego los numeros usados
            num_minuendo= int(input("Digite el minuendo de la resta: "))
            num_sustraendo= int(input("Digite el sustraendo de la resta: "))
            #agrega los numeros y los guarda en un archivo
            lista_resta.append(num_minuendo)
            lista_resta.append(num_sustraendo)
            agregar_archivo.agregar_numeros(str(lista_resta))
            #invoca el método de resta
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
            #guarda los numeros en un archivo
            agregar_archivo.agregar_numeros(lista_multiply)
            #invoca al método de multiplicación
            multiplicacion= aritméticas2.calcular_multiplicar(lista_multiply)
            print(f"El resultado de la multiplicación es: {multiplicacion}")#imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(multiplicacion))
        #ejecuta la división
        elif opcion== "/":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide los numeros al usuario
            lista_division=[] #lista para guardar luego los numeros usados
            num_dividendo= int(input("Digite el dividendo de la división: "))
            num_divisor= int(input("Digite el divisor de la divsión: "))
            #agrega los numeros y los guarda en un archivo
            lista_division.append(num_dividendo)
            lista_division.append(num_divisor)
            agregar_archivo.agregar_numeros(str(lista_division))
            #invoca el método de division
            division= aritméticas2.calcular_division(num_dividendo, num_divisor)
            print(f"El resultado de la división es: {division}") #imprime el resultado
            #guarda el resultado en un archivo
            agregar_archivo.agregar_resultados(str(division))
        #ejecuta el factorial
        elif opcion== "!":
            #guarda la operacion en un archivo
            agregar_archivo.agregar_operaciones(opcion)
            #pide el numero al usuario
            num_factorial= int(input("Calcular el factorial del siguiente numero positivo: "))
            #guarda el numero en un archivo
            agregar_archivo.agregar_numeros(num_factorial)
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
            lista_potencia=[] #lista para guardar luego los numeros usados
            num_base= int(input("Digite la base de la potencia: "))
            num_exponente= int(input("Digite el exponente de la potencia: "))
            #agrega los numeros y los guarda en un archivo
            lista_potencia.append(num_base)
            lista_potencia.append(num_exponente)
            agregar_archivo.agregar_numeros(str(lista_potencia))
            #invoca el método de potencia
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