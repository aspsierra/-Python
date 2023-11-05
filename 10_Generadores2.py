def devuelveCiudades(*ciudades):    #! el * quiere decir que el elemento e recibir es una tupla de longitud indeterminada
    for el in ciudades:
        #for subEl in el:
            yield from  el #! Con Yield from accedemos a los subelementos, en este caso a las letras de cada palabra


ciudades = devuelveCiudades("Madrid", "Barcelona", "Vigo")

print(next(ciudades))
print(next(ciudades))