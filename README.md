# archivos

Mi dirección de GitHub para este repositorio es la siguiente: [GitHub](https://github.com/lauralardies/archivos)
https://github.com/lauralardies/archivos

Aquí tenemos el código de la clase Calificaciones(), que es capaz de hacer tres acciones:
1 - Lee el archivo csv y ordena todos los datos en una lista de diccionarios ordenados alfabéticamente por los apellidos de los alumnos.
2 - Calcula la nota final de cada alumno teniendo en cuenta que cada parcial vale un 30% y las prácticas un 40%
3 - Crea dos listas, una de alumnos suspensos y otra de aprobados, teniendo en cuenta su asistencia, nota en los exámenes y nota final.

```
from operator import itemgetter

class Calificaciones():
    
    def valor_cambiado(self, valor): # Esta función sirve para que podamos hacer cálculos con los valores de las notas.

        # Para aquellas notas que estén vacías (es decir, en la casilla no haya nada) las tenemos que sustituir por 0.
        # Para ello verificamos si hay algún número en la casilla. Si no hay ninguno, sustituimos ese vacío por 0.
        if any(chr.isdigit() for chr in valor) == False:
            valor = 0.0
            return valor

        # En el caso de que sí haya nota, para poder operarla luego, necesitamos cambiar las comas por puntos.
        # Esto es debido a que los float en Python llevan puntos y no comas.
        valor = valor.replace(",", ".")
        return valor

    def leer_fichero(self, fichero):

        with open(fichero, "r", encoding="utf-8") as archivo:
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
                                ("Parcial1", self.valor_cambiado(lista[3])),
                                ("Parcial2", self.valor_cambiado(lista[4])),
                                ("Ordinario1", self.valor_cambiado(lista[5])),
                                ("Ordinario2", lista[6]),
                                ("Prácticas", self.valor_cambiado(lista[7])),
                                ("OrdinarioPracticas", self.valor_cambiado(lista[8])),
                ])
                lista_dict.append(diccionario) # Añadimos cada diccionario generado cada vez que se ejecuta el bucle for a la variable lista.
        
        return sorted(lista_dict, key=itemgetter("Apellidos")) # Nos permite ordenar el diccionario alfabéticamente por apellidos.

    def nota_final(self, lista):

        for i in range(0, len(lista)):
            # Creamos una nueva entrada en el diccionario, llamado NotaFinal, en el cual está calculada la nota final del curso.
            lista[i]["NotaFinal"] = float(lista[i]["Parcial1"]) * 0.3 + float(lista[i]["Parcial2"]) * 0.3 + float(lista[i]["Prácticas"]) * 0.4

        return lista # Devolvemos la nueva lista de diccionarios que ahora contiene una nueva celda, la de la nota final.

    def suspensos_aprobados(self, lista):
        suspensos = []
        aprobados = []
        for i in range(0, len(lista)):
            # Primero comprobamos la asistencia de nuestro alumno.
            if (lista[i]["Asistencia"]) >= "75%":
                # Ahora tomamos en cuenta que la nota mínima de los exámenes es de 4 y que la nota final debe de ser superior o igual a 5
                if float(lista[i]["Parcial1"]) >= 4.0 and float(lista[i]["Parcial2"]) >= 4.0 and float(lista[i]["Prácticas"]) >= 4.0 and float(lista[i]["NotaFinal"]) >= 5.0:
                    aprobados.append(lista[i]["Apellidos"] + ", " + lista[i]["Nombre"])
                else:
                    suspensos.append(lista[i]["Apellidos"] + ", " + lista[i]["Nombre"])
            else:
                suspensos.append(lista[i]["Apellidos"] + ", " + lista[i]["Nombre"])
            
        return suspensos, aprobados
```

Y aquí tenemos el código principal que permite que se ejecute la clase que acabamos de ver:
```
from archivos import Calificaciones

test = Calificaciones()
lista = test.leer_fichero("calificaciones.csv")
nota_final = test.nota_final(lista)
suspensos, aprobados = test.suspensos_aprobados(nota_final)
print("Han suspendido los siguientes alumnos:\n" + str(suspensos) + "\nHan aprobado los siguientes alumnos:\n" + str(aprobados))
```
