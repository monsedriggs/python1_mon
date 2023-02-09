#agrega la operación
def agregar_operaciones(operacion):
    #abre el archivo
    archivo= open("resultados.txt", "a")
    archivo.write(f"La operacion realizada fue: {operacion}")
    archivo.write(",")
    #cerrar el archivo
    archivo.close()

#agrega los numeros 
def agregar_numeros(numeros):
    #abre el archivo
    archivo= open("resultados.txt", "a")
    archivo.write(f" Los numeros utilizados en la operacion son: {numeros}")
    archivo.write(",")
    #cierra el archivo
    archivo.close()

#agrega el resultado
def agregar_resultados(resultado):
    #abre el archivo
    archivo= open("resultados.txt", "a")
    archivo.write(f" El resultado es: {resultado}")
    archivo.write(f"\n")
    #cerrar el archivo
    archivo.close()
