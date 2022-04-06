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
        
        return sorted(lista_dict, key=itemgetter("Apellidos")) # Nos permite ordenar el diccionario alfabéticamente por apellidos

    def nota_final(self, lista):

        for i in range(0, len(lista)):

            # Para operar en Python, los float tienen puntos no comas, en las siguientes líneas reemplazamos las comas por los puntos
            parcial1 = (lista[i]["Parcial1"]).replace(",", ".")
            parcial2 = (lista[i]["Parcial2"]).replace(",", ".")            
            practicas = (lista[i]["Prácticas"]).replace(",", ".")

            # Ahora, para aquellas notas que estén vacías (es decir, en la casilla no haya nada) las tenemos que sustituir por 0
            # Para ello verificamos si hay algún número en la casilla. Si no hay ninguno, sustituimos ese vacío por 0.
            if any(chr.isdigit() for chr in parcial1) == False:
                parcial1 = 0.0
            
            if any(chr.isdigit() for chr in parcial2) == False:
                parcial2 = 0.0

            if any(chr.isdigit() for chr in practicas) == False:
                practicas = 0.0

            # Por último creamos una nueve entrada en el diccionario, llamado NotaFinal, en el cual está calculada la nota final
            lista[i]["NotaFinal"] = float(parcial1) * 0.3 + float(parcial2) * 0.3 + float(practicas) * 0.4

        return lista # Devolvemos la nueva lista de diccionarios que ahora contiene una nueva celda, la de la nota final

    def suspensos_aprobados(self, lista):
        suspensos = []
        aprobados = []
        for i in range(0, len(lista)):
            if (lista[i]["Asistencia"]) >= "75%":

                # Para poder pasar a float en la siguiente comparación, las comas tienen que pasar a ser números
                parcial1 = (lista[i]["Parcial1"]).replace(",", ".")
                parcial2 = (lista[i]["Parcial2"]).replace(",", ".")            
                practicas = (lista[i]["Prácticas"]).replace(",", ".")

                # Otra vez, tenemos que convertir aquellas casillas vacías en 0
                if any(chr.isdigit() for chr in parcial1) == False:
                    parcial1 = 0.0
                
                if any(chr.isdigit() for chr in parcial2) == False:
                    parcial2 = 0.0

                if any(chr.isdigit() for chr in practicas) == False:
                    practicas = 0.0

                # Ahora tomamos en cuenta que la nota mínima de los exámenes es de 4 y que la nota final debe de ser superior o igual a 5
                if float(parcial1) >= 4.0 and float(parcial2) >= 4.0 and float(practicas) >= 4.0 and float(lista[i]["NotaFinal"]) >= 5.0:
                    aprobados.append(lista[i]["Apellidos"])
                    aprobados.append(lista[i]["Nombre"])

                else:
                    suspensos.append(lista[i]["Apellidos"])
                    suspensos.append(lista[i]["Nombre"])

            else:
                suspensos.append(lista[i]["Apellidos"])
                suspensos.append(lista[i]["Nombre"])
            
        return suspensos, aprobados