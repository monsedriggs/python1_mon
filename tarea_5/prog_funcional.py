'''
Funciones que calculan el cubo de cada numero en una lista
La función realizada con programación funcional recibe como función una funcion lambda que eleva a la 3 el numero, de iterable recibe una lista que genera numeros random cada vez. Y devuelve la lista con cada elemento elevado al cubo
'''
#Función original
import random

#Genera una lista de numero aleatorios
lista_random= random.sample(range(100), 3)
print(lista_random)

#Crea nueva lista para guardar los numeros al cubo
lista_al_cubo=[]
for num in lista_random: 
    #Calcula el cubo de cada numero en la lista random
    cubo= num**3
    lista_al_cubo.append(cubo)
print(lista_al_cubo)

#Nueva función
print(list(map(lambda n: n**3, lista_random)))

'''
Funciones que eliminan un elemento especifico de una lista
La función realizada con programacion funcional recibe una función lambda que indica la condición para el filtrado de los elementos de la lista. Devuelve una nueva lista sin el elemento especificado
'''
#Función original
def eliminar_elementos(lista_elementos, eliminado):
    for i in lista_elementos:
        if i == eliminado:
            lista_elementos.remove(eliminado)
    print(lista_elementos)
   
eliminar_elementos([20,30,40,20,5,100,5,20],20)
eliminar_elementos([25,36,88,22,9,88,16,88],88)
eliminar_elementos(["perro","gato","sombrero","gato","zanahoria"],"gato")
eliminar_elementos(["manzana","pastel","harina","pastel","huevo"],"pastel")

#Nueva función
print(list(filter(lambda e: e!=20,[20,30,40,20,5,100,5,20] )))
print(list(filter(lambda e: e!=88,[25,36,88,22,9,88,16,88] )))
print(list(filter(lambda e: e!="gato",["perro","gato","sombrero","gato","zanahoria"] )))
print(list(filter(lambda e: e!="pastel",["manzana","pastel","harina","pastel","huevo"] )))

'''
Funciones que restan dos numeros
La funcion lambda recibe dos parametros, y luego los resta entre sí. Devuelve el resultado de la resta
'''
#Funcion original
def calcular_resta( num_1, num_2):
    return num_1 - num_2

print(calcular_resta(10,14))
print(calcular_resta(4,5))
print(calcular_resta(782,49))

#Nueva funcion
print((lambda a,b: a-b)(10,14))
print((lambda a,b: a-b)(4,5))
print((lambda a,b: a-b)(782,49))

'''
Funciones que dividen dos numeros
La funcion lambda recibe dos numeros, y los divide entre sí. Devuelve el resultado de la division entera de los parametros.
'''
#Funcion original
def calcular_division(num_1, num_2):
    return num_1 // num_2

print(calcular_division(25,5))
print(calcular_division(80,6))
print(calcular_division(699,70))

#Nueva funcion
print((lambda a,b: a//b)(25,5))
print((lambda a,b: a//b)(80,6))
print((lambda a,b: a//b)(699,70))