#Pide el numero al usuario
num= int(input("Ingrese un numero entero mayor que 0: \n"))

#Inicializa un contador en cero
x=0
#Si el numero es menor o igual que cero, error
if num<=0:
        print(f"Error, el numero ingresado debe ser mayor que 0")
else:
    #Loop para imprimir el triangulo
    triangulo= ""
    for x in range(1,num+1):
        triangulo += str(x)+" "
        print(triangulo)
    
