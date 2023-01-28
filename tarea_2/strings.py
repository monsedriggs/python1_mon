#Pide al usuario las frases
string_1= str(input("Ingrese la primer palabra: "))
string_2= str(input("Ingrese la segunda palabra, del mismo largo de la primera: "))


#Si las frases no son del mismo tamaño, error
if len(string_2) != len(string_1):
    print(f"\nError, las palabras deben tener el mismo largo")
else:
    #Inicializa un contador en cero
    x=0
    #Variable para la nueva palabra
    nueva_string= ""
    while x < len(string_1):
        nueva_string+=string_1[x]+string_2[x]
        x+=1
    print(f"\n{nueva_string}")