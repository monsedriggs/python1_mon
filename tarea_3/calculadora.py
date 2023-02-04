import aritméticas2
import agregar_resultados

def correr():
   while True:
        opcion= input("\t+) Suma\n\t-) Resta\n\t*) Multiplicación\n\t//) División\n\t!) Factorial\n\t^) Potencia\n\t~) Salir\nIngrese una opción: ")
        #ejecuta la suma
        if opcion== "+":
            #pide los numeros al usuario
            lista_suma= []
            num_suma= int("Digite el numero por sumar (0 para terminar): ")
            while num_suma !=0:
                lista_suma.append(num_suma)
                num_suma= int("Digite el numero por sumar (0 para terminar): ")
            suma= aritméticas2.calcular_suma(lista_suma)
            print(f"El resultado de la suma es:{suma} ")#imprime el resultado
            resultado_suma= agregar_resultados.agregar_resultados(suma)
            pass
        #ejecuta la resta
        elif opcion== "-":
            #pide los numeros al usuario
            num_minuendo= int(input("Digite el minuendo de la resta: "))
            num_sustraendo= int(input("Digite el sustraendo de la resta: "))
            print(f"El resultado de la resta es: ")#imprime el resultado
            pass
        #ejecuta la multiplicación
        elif opcion== "*":
            #pide los numeros al usuario
            print(f"El resultado de la multiplicación es: ")#imprime el resultado
            pass
        #ejecuta la división
        elif opcion== "//":
            #pide los numeros al usuario
            num_dividendo= int(input("Digite el dividendo de la división: "))
            num_divisor= int(input("Digite el divisor de la divsión: "))
            print(f"El resultado de la división es: {aritméticas2.calcular_division(num_dividendo, num_divisor)}") #imprime el resultado
        #ejecuta el factorial
        elif opcion== "!":
            #pide el numero al usuario
            num_factorial= int(input("Calcular el factorial de: "))
            if num_factorial<0:
                print("Error, el numero debe ser entero positivo")
            else:
                print(f"El factorial es: {aritméticas2.calcular_factorial(num_factorial)}")#imprime el resultado
        #ejecuta la potencia
        elif opcion== "^":
            #pide los numeros al usuario
            num_base= int(input("Digite la base de la potencia: "))
            num_exponente= int(input("Digite el exponente de la potencia: "))
            print(f"La potencia es: {aritméticas2.calcular_potencia(num_base, num_exponente)}")#imprime el resultado
        #salir
        elif opcion== "~":
            break
        else:
            print("Error, opción invalida, intente de nuevo")
        print()
correr()