#Diccionario principal
sample_dict= {
    "class":{
        "student":{
            "name": "Mike",
            "marks":{
                "physics": 70,
                "history": 80,
                "math": 90
            }
        }
    }
}
#Variable que guarda el nombre del estudiante
nombre= sample_dict["class"]["student"]["name"]
#Cantidad de materias en el diccionario
cantidad_materias= len(sample_dict["class"]["student"]["marks"])
#Calcula el promedio de todas las notas 
suma_notas= 0
for x in sample_dict["class"]["student"]["marks"].values():
    suma_notas += x
    promedio_notas= suma_notas/cantidad_materias
#Nuevo diccionario con el nombre y el promedio de notas del estudiante
promedio_dict= {
    nombre: promedio_notas
}
print(promedio_dict)