#Lista con numeros repetidos
repetidos= [2,4,4,6,6,8,12]

#Nueva lista sin repetidos
sin_repetidos= []
for i in repetidos:
    if i not in sin_repetidos:
        sin_repetidos.append(i)
print(sin_repetidos) 