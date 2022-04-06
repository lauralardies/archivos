from archivos import Calificaciones

test = Calificaciones()
lista = test.leer_fichero("calificaciones.csv")
nota_final = test.nota_final(lista)
suspensos, aprobados = test.suspensos_aprobados(nota_final)
print("Han suspendido los siguientes alumnos:\n" + str(suspensos) + "\nHan aprobado los siguientes alumnos:\n" + str(aprobados))