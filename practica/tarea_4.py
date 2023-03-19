#Cuenta los tipos de elementos en un string
def contar_tipos(string):
    letras=0
    numeros=0
    especiales=0
    for i in string:
        if i.isalpha():
            letras+=1
        elif i.isnumeric():
            numeros+=1
        else:
            especiales+=1
    print(f"Letras= {letras}\nNumeros= {numeros}\nCaracteres especiales= {especiales}")

contar_tipos("P@#yn26at^&i5ve")
contar_tipos("Nw0&8me#oi")
contar_tipos("palusA")
contar_tipos("9867")
contar_tipos("#^*%")

#Cuenta todas las apariciones de cada caracter
def contar_caracteres(string):
    caracter_dict={}
    for elemento in string:
        if elemento.lower()in caracter_dict:
            caracter_dict[elemento.lower()]+=1
        else:
            caracter_dict[elemento.lower()]=1
    print(caracter_dict)

contar_caracteres("papaya")
contar_caracteres("aguacate")
contar_caracteres("Albaricoque")
contar_caracteres("meLlizAs")

#Elimina todas las apariciones de un elemento
def eliminar_elementos(lista_elementos, eliminado):
    for i in lista_elementos:
        if i == eliminado:
            lista_elementos.remove(eliminado)
    print(lista_elementos)
   
eliminar_elementos([20,30,40,20,5,100,5,20],20)
eliminar_elementos([25,36,88,22,9,88,16,88],88)
eliminar_elementos(["perro","gato","sombrero","gato","zanahoria"],"gato")
eliminar_elementos(["manzana","pastel","harina","pastel","huevo"],"pastel")

#Crea una lista y una tupla de una entrada 
def crear_lista_tupla(numeros):
    list_numeros=numeros.split(",")
    tuple_numeros=tuple(list_numeros)
    print(f"Lista: {list_numeros}\nTupla: {tuple_numeros}")

crear_lista_tupla("1,2,3,4,5,6")
crear_lista_tupla("5,10,15,20,25")
crear_lista_tupla("7,8,9,10")
crear_lista_tupla("9,27,18,21")

