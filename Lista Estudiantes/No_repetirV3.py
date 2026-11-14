"""
Nombre del archivo: No_repetirV2.py
Descripción: Captura la calificación de n estudiantes y las almacene en una lista. Calcula el promedio de las calificaciones capturadas y después presenta el promedio grupal, lista todos los estudiantes (por número) que tienen una calificación superior al promedio grupal.
Autor: Diego Nava Hernandez
Fecha: 06/11/2026
"""

estudiantes = int(input("Ingrese la cantidad de estudiantes > "))

alumnos = []
##Captura los nombres de los estudiantes junto a sus calificaciones.
for i in range(estudiantes):
    nom = input("\nIngrese el nombre del estudiante > ")
    n = int(input("\nIngrese la calificación > "))
    alumnos.append([nom, n])


suma = 0
for i in range(len(alumnos)):
    suma += alumnos[i][1]
    
prom = suma / estudiantes

print("El promedio grupal es: ", prom)

sobresalientes = []

for i in range(len(alumnos)):
    if alumnos[i][1] > prom:
        sobresalientes.append(alumnos[i][0])
        
print()
print("Estudiantes con calificación superior al promedio:")
print(sobresalientes)