#agrega la operación
def agregar_operaciones(operacion):
    #abre el archivo
    archivo= open("resultados.txt", "a")
    archivo.write(operacion)
    archivo.write(",")
    #cerrar el archivo
    archivo.close()


#agrega el resultado
def agregar_resultados(resultado):
    #abre el archivo
    archivo= open("resultados.txt", "a")
    archivo.write(resultado)
    archivo.write(f"\n")
    #cerrar el archivo
    archivo.close()
