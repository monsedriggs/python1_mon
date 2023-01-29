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