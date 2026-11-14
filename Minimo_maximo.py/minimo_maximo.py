def es_mayor(n1:int, n2:int,n3:int):
    """
        Calcula el minimo y maximo de 3 numeros. 

        Parameters: 

            n1(int): Número entero necesario para la comparación. 

            n2(int): Número entero necesario para la comparación.
            
            n3(int): Número entero necesaria para la comparación. 
            
        Returns: 

            mayor: Regresa el valor mas alto de los 3 numeros.
            
        Raises:
        
            TypeError: Si se detecta texto o decimal . 

        Examples: 

            >>> es_mayor(3,2,1)

            3

            >>> es_mayor(1,-1,0)
                
            1
            
            >>> es_mayor(lol,1,3)
            Traceback (most recent call last):
               TypeError: Lo valores deben ser enteros

            >>> es_mayor(12, 3.3, 1)
            
            Traceback (most recent call last):
                TypeError: Lo valores deben ser enteros
    """ 
    if not isinstance(n1, int) or not isinstance(n2, int) or not isinstance(n3, int):
        raise TypeError("Lo valores deben ser enteros")
    
    mayor = n1
    if  n2 >= mayor:
        mayor = n2
    if n3 >= mayor:
        mayor=n3
    return mayor
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
"""
Archivo: minimo_maximo.py
Descripción: Programa que muestra el mayor de 3 numeros.
Autor: Xxmater360
Fecha: 29/10/2026
"""


while True:
    try:
        n1 = int(input("Ingresa el primero digito: "))
    except ValueError:
        print("Solo valores enteros")
        continue
    break
    
while True:
    try:
        n2 = int(input("Ingresa el segundo digito: "))
    except ValueError:
        print("Solo valores enteros")
        continue
    break

while True:
    try:
        n3 = int(input("Ingresa el tercer digito: "))
    except ValueError:
        print("Solo valores enteros")
        continue
    break

print("El numero mayor es: ", es_mayor(n1,n2,n3))