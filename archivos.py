from operator import itemgetter

class Calificaciones():

    def leer_fichero(self, fichero):
        with open(fichero, "r") as archivo:
            next(archivo, None) # Esta función nos permite saltarnos la primera fila, donde aparece el encabezado
            lista_dict = [] # Creamos una lista vacía donde guardar nuestros diccionarios
            for linea in archivo: # Ahora vamos a anaizar linea por linea
                linea = linea.rstrip() # Elimina el salto de línea
                lista = linea.split(";") # Cada columna se almacena en una lista
                # En la siguiente linea creamos los diccionarios para cada alumno
                diccionario = dict([
                                ("Apellidos", lista[0]),
                                ("Nombre", lista[1]),
                                ("Asistencia", lista[2]),
                                ("Parcial1", lista[3]),
                                ("Parcial2", lista[4]),
                                ("Ordinario1", lista[5]),
                                ("Ordinario2", lista[6]),
                                ("Prácticas", lista[7]),
                                ("OrdinarioPracticas", lista[8]),
                ])
                lista_dict.append(diccionario) # Añadimos cada diccionario generado cada vez que se ejecuta el bucle for a la variable lista
        
        return sorted(lista_dict, key=itemgetter("Apellidos"))

test = Calificaciones()
print(test.leer_fichero("calificaciones.csv"))