 #Recibe un numero del usuario
#imprime todos los numeros del 1 al num ingresado
#los multiplos de 3 imprime "Fizz"
#los multiplos de 5 imprime "Buzz"
#los multiplos de ambos imprime "FizzBuzz"

num= int(input("Ingrese numero entero mayor a 0\n"))

x=0
for x in range(1,(num)+1):
    #NOTA: recordar que entran en la primera que coincidan!!
    if x%3==0 and x%5==0:
        print(f"FizzBuzz")
    elif x %3==0:
        print(f"Fizz")
    elif x %5==0:
        print(f"Buzz")
    else:
        print(f"{x}")
