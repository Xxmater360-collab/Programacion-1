"""
    Invierte una cadena de texto. 

    Parameters: 

        cadena(str): Cadena de texto a invertir. 

    Returns: 

        str: Regresa la cadena proporcionada alreves.
        
    Raises:

    Examples: 

        >>> Invertir_cadena(Fruti)
            iturF

        >>> Invertir_cadena(Granada)
            adanarG
            
        >>> Invertir_cadena(Panzer 4 "PRUSSIA")
            "AISSURP" 4 reznaP
"""

def Invertir_cadena(cadena:str) -> str:
    
    return cadena[::-1]




#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
"""
Archivo: palabra_invertida.py
Descripción: Programa que devuelve una cadena alreves.
Autor: Diego Nava Hernandez
Fecha: 29/10/2026
"""


cadena = input("Ingresa la cadena: \n")

print("Cadena invertia = ", Invertir_cadena(cadena))