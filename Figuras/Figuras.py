"""
Archivo: Figuras.py
Descripción:
Autores: Xxmater360
Fecha: 03/11/2026
"""

from sys import stderr

def crear_reloj(dim : int, simbolo : str, hueco : bool = False) -> str:
    """
    Crea un reloj de arena en cadenas de carácteres.
    
    Parameters:
    
        dim (int): El ancho de la figura.
        simbolo (str): El símbolo qué se va a usar para dar forma a la figura.
        hueco (bool, opciónal): Si es True, remueve los símbolos del interior de la figura. Por defecto es False.
        
    Returns:
    
        str: El reloj de arena en cadenas de carácteres.
        
    Raises:
    
        TypeError: Si el tipo de alguno de los parámetros es incorrecto.
        ValueError: Si el argumento dim no es impar, si el argumento dim es menor a 5, si el argumento símbolo no es un solo carácter.
        
    Examples:
    
        >>> crear_reloj(7, "a")
        'aaaaaaa\n aaaaa \n  aaa  \n   a   \n  aaa  \n aaaaa \naaaaaaa\n'
        >>> crear_reloj(11, "*", True)
        '***********\n *       * \n  *     *  \n   *   *   \n    * *    \n     *     \n    * *    \n   *   *   \n  *     *  \n *       * \n***********\n'
        >>> crear_reloj(2, "r")
        Traceback (most recent call last):
        ...
        ValueError: El argumento dim debe ser mayor o igual que 5.
    """
    # Verificar los tipos de cada argumento.
    if not isinstance(dim, int):
        raise TypeError("Tipo inesperado para dim, se esperaba un entero")
    if not isinstance(simbolo, str):
        raise TypeError("Tipo inesperado para símbolo, se esperaba una cadena")
    if not isinstance(hueco, bool):
        raise TypeError("Tipo inesperado para hueco, se esperaba un booleano")
    
    # Checar qué los valores de los argumentos sean correctos.
    if dim < 5:
        raise ValueError("El argumento dim debe ser mayor o igual que 5")
    if dim % 2 == 0:
        raise ValueError("El argumento dim debe ser impar")
    if len(simbolo) != 1:
        raise ValueError("El argumento símbolo debe contener exactamente un carácter")
    
    reloj = ""
    
    if not hueco:
        # Concatenar el triángulo invertido.
        for i in range(dim, 0, -2):
            reloj += f"{(simbolo*i):^{dim}}\n"
        # Concatenar el triángulo normal, sin colocar la punta.
        for i in range(3, dim+1, 2):
            reloj += f"{(simbolo*i):^{dim}}\n"
    else:
        # Concatenar la parte de arriba
        reloj += simbolo*dim + "\n" 
        # Concatenar las demás partes del triángulo invertido, colocando los símbolos en los extremos y rellenando con espacios.
        for i in range(dim-4, 0, -2):
            reloj += f"{(simbolo + " "*i + simbolo):^{dim}}\n"
        # Concatenar el vértice de la figura.
        reloj += f"{simbolo:^{dim}}\n"
        # Concatenar las partes del triángulo normal, colocando los símbolo en los extremos y rellenando con espacios.
        for i in range(1, dim-2, 2):
            reloj += f"{(simbolo + " "*i + simbolo):^{dim}}\n"
        # Concatenar la parte de abajo.
        reloj += simbolo*dim + "\n"
        
    return reloj

def crear_rombo(dim : int, simbolo : str, hueco : bool = False) -> str:
    """
    Crea un rombo en cadenas de carácteres.
    
    Parameters:
    
        dim (int): El ancho de la figura.
        simbolo (str): El símbolo qué se va a usar para dar forma a la figura.
        hueco (bool, opciónal): Si es True, remueve los símbolos del interior de la figura. Por defecto es False.
        
    Returns:
    
        str: El rombo en cadenas de carácteres.
        
    Raises:
    
        TypeError: Si el tipo de alguno de los parámetros es incorrecto.
        ValueError: Si el argumento dim no es impar, si el argumento dim es menor a 5, si el argumento símbolo no es un solo carácter.
        
    Examples:
    
        >>> crear_rombo(9, "/")
        '    /    \n   ///   \n  /////  \n /////// \n/////////\n /////// \n  /////  \n   ///   \n    /    \n'
        >>> crear_rombo(13, "*", True)
        '      *      \n     * *     \n    *   *    \n   *     *   \n  *       *  \n *         * \n*           *\n *         * \n  *       *  \n   *     *   \n    *   *    \n     * *     \n      *      \n'
        >>> crear_rombo(10.2, "*")
        Traceback (most recent call last):
        ...
        TypeError: Tipo inesperado para dim, se esperaba un entero
    """
    # Verificar los tipos de cada argumento.
    if not isinstance(dim, int):
        raise TypeError("Tipo inesperado para dim, se esperaba un entero")
    if not isinstance(simbolo, str):
        raise TypeError("Tipo inesperado para símbolo, se esperaba una cadena")
    if not isinstance(hueco, bool):
        raise TypeError("Tipo inesperado para hueco, se esperaba un booleano")
    
    # Checar qué los valores de los argumentos sean correctos.
    if dim < 5:
        raise ValueError("El argumento dim debe ser mayor o igual que 5")
    if dim % 2 == 0:
        raise ValueError("El argumento dim debe ser impar")
    if len(simbolo) != 1:
        raise ValueError("El argumento símbolo debe contener exactamente un carácter")
    
    rombo = ""
    
    if not hueco:
        # Concatenar el triángulo normal, sin la base.
        for i in range(1, dim-1, 2):
            rombo += f"{(simbolo*i):^{dim}}\n"
        # Concatenar el triángulo invertido.
        for i in range(dim, 0, -2):
            rombo += f"{(simbolo*i):^{dim}}\n"
    else:
        # Concatenar la parte de arriba
        rombo += f"{simbolo:^{dim}}\n"
        # Concatenar las partes del triángulo normal, colocando los símbolo en los extremos y rellenando con espacios.
        for i in range(1, dim-2, 2):
            rombo += f"{(simbolo + " "*i + simbolo):^{dim}}\n"
        # Concatenar la parte de en medio.
        rombo += simbolo + " "*(dim-2) + f"{simbolo}\n"
        # Concatenar las demás partes del triángulo invertido, colocando los símbolos en los extremos y rellenando con espacios.
        for i in range(dim-4, 0, -2):
            rombo += f"{(simbolo + " "*i + simbolo):^{dim}}\n"
        # Concatenar la parte de abajo.
        rombo += f"{simbolo:^{dim}}\n" 
            
    return rombo

def crear_monio(dim : int, simbolo : str, hueco : bool = False) -> str:
    """
    Crea un moño en cadenas de carácteres.
    
    Parameters:
    
        dim (int): El ancho de la figura.
        simbolo (str): El símbolo qué se va a usar para dar forma a la figura.
        hueco (bool, opciónal): Si es True, remueve los símbolos del interior de la figura. Por defecto es False.
        
    Returns:
    
        str: El moño en cadenas de carácteres.
        
    Raises:
    
        TypeError: Si el tipo de alguno de los parámetros es incorrecto.
        ValueError: Si el argumento dim no es impar, si el argumento dim es menor a 5, si el argumento símbolo no es un solo carácter.
        
    Examples:
    
        >>> crear_monio(5, "@")
        '@   @\n@@ @@\n@@@@@\n@@ @@\n@   @\n'
        >>> crear_monio(17, "t", True)
        'ttttttttttttttttt\n t             t \n  t           t  \n   t         t   \n    t       t    \n     t     t     \n      t   t      \n       t t       \n        t        \n       t t       \n      t   t      \n     t     t     \n    t       t    \n   t         t   \n  t           t  \n t             t \nttttttttttttttttt\n'
        >>> crear_monio(21, "")
        Traceback (most recent call last):
        ...
        ValueError: El argumento símbolo debe contener exactamente un carácter
    """
    # Verificar los tipos de cada argumento.
    if not isinstance(dim, int):
        raise TypeError("Tipo inesperado para dim, se esperaba un entero")
    if not isinstance(simbolo, str):
        raise TypeError("Tipo inesperado para símbolo, se esperaba una cadena")
    if not isinstance(hueco, bool):
        raise TypeError("Tipo inesperado para hueco, se esperaba un booleano")
    
    # Checar qué los valores de los argumentos sean correctos.
    if dim < 5:
        raise ValueError("El argumento dim debe ser mayor o igual que 5")
    if dim % 2 == 0:
        raise ValueError("El argumento dim debe ser impar")
    if len(simbolo) != 1:
        raise ValueError("El argumento símbolo debe contener exactamente un carácter")
    
    monio = ""
    # Calcular la dimensión de los triángulos rectangulos qué conforman la figura.
    a = dim//2
    
    if not hueco:
        # Concatenar los triángulos de arriba.
        for i in range(1, a+1):
            monio += f"{(simbolo*i):<{a}} {(simbolo*i):>{a}}\n"
        # Concatenar la parte de en medio.
        monio += simbolo*dim + "\n"
        # Concatenar los triángulos de abajo.
        for i in range(a, 0, -1):
            monio += f"{(simbolo*i):<{a}} {(simbolo*i):>{a}}\n"
    else:
        # Concatenar los primeros dos puntos de arriba.
        monio += f"{simbolo:<{a}} {simbolo:>{a}}\n"
        # Concatenar los triángulos de arriba sin relleno.
        for i in range(0, a-1):
            monio += f"{(simbolo + " "*i + simbolo):<{a}} {(simbolo + " "*i + simbolo):>{a}}\n"
        # Concatenar la parte de en medio.
        monio += f"{simbolo:<{a}}{simbolo}{simbolo:>{a}}\n"
        # Concatenar los triángulos de abajo sin relleno.
        for i in range(a-2, -1, -1):
            monio += f"{(simbolo + " "*i + simbolo):<{a}} {(simbolo + " "*i + simbolo):>{a}}\n"
        # Concatenar los ultimos dos puntos de abajo.
        monio += f"{simbolo:<{a}} {simbolo:>{a}}\n"
        
    return monio

def crear_copa(dim : int, simbolo : str, hueco : bool = False) -> str:
    """
    Crea una copa en cadenas de carácteres.
    
    Parameters:
    
        dim (int): El ancho de la figura.
        simbolo (str): El símbolo qué se va a usar para dar forma a la figura.
        hueco (bool, opciónal): Si es True, remueve los símbolos del interior de la figura. Por defecto es False.
        
    Returns:
    
        str: La copa en cadenas de carácteres.
        
    Raises:
    
        TypeError: Si el tipo de alguno de los parámetros es incorrecto.
        ValueError: Si el argumento dim no es impar, si el argumento dim es menor a 5, si el argumento símbolo no es un solo carácter.
        
    Examples:
    
        >>> crear_copa(11, "$")
        '$$$$$$$$$$$\n $$$$$$$$$ \n  $$$$$$$  \n   $$$$$   \n    $$$    \n     $     \n     $     \n     $     \n     $     \n$$$$$$$$$$$\n'
        >>> crear_copa(5, "%", True)
        '%%%%%\n % % \n  %  \n  %  \n  %  \n%%%%%\n'
        >>> crear_copa(10, "#")
        Traceback (most recent call last):
        ...
        ValueError: El argumento dim debe ser impar
    """
    # Verificar los tipos de cada argumento.
    if not isinstance(dim, int):
        raise TypeError("Tipo inesperado para dim, se esperaba un entero")
    if not isinstance(simbolo, str):
        raise TypeError("Tipo inesperado para símbolo, se esperaba una cadena")
    if not isinstance(hueco, bool):
        raise TypeError("Tipo inesperado para hueco, se esperaba un booleano")
    
    # Checar qué los valores de los argumentos sean correctos.
    if dim < 5:
        raise ValueError("El argumento dim debe ser mayor o igual que 5")
    if dim % 2 == 0:
        raise ValueError("El argumento dim debe ser impar")
    if len(simbolo) != 1:
        raise ValueError("El argumento símbolo debe contener exactamente un carácter")
    
    copa = ""
    
    if not hueco:
        # Concatenar la taza de la copa.
        for i in range(dim, 0, -2):
            copa += f"{(simbolo*i):^{dim}}\n"
    else:
        # Concatenar la parte de arriba de la taza de la copa.
        copa += simbolo*dim + "\n"
        # Concatenar el resto de la taza de la copa sin relleno.
        for i in range(dim-4, 0, -2):
            copa += f"{(simbolo + " "*i + simbolo):^{dim}}\n"
            
    # Concatenar el mango y la base de la copa.
    copa += (f"{simbolo:^{dim}}" + "\n")*3 + simbolo*dim + "\n"
    
    return copa

#######################################################################################
################################## PROCESO PRINCIPAL ##################################
#######################################################################################
if __name__ == "__main__":
    dim_max = 149

    while True:
        # Desplegar menu
        print("""0) Salir
    1) Reloj de arena
    2) Rombo
    3) Moño
    4) Copa
    5) Todas las figuras""")
        
        # Capturar la opción.
        while True:
            try:
                opc = int(input("¿qué figura desea imprimir? (0-5): "))
                if 0 <= opc <= 5:
                    break
                print("opción inválida")
            except ValueError:
                print("Error: El valor ingresado debe ser un entero", file=stderr)
            except:
                print("Ha ocurrido un error inesperado")
                
        # Verificar si la opción es 0 para terminar el programa antes de capturar los demás datos.
        if opc == 0:
            print("Saliendo...")
            break
        
        # Capturar la dimensión de la figura.
        while True:
            try:
                dimension = int(input("Dimensión: "))
                if 5 <= dimension <= dim_max and dimension % 2 != 0:
                    break
                print(f"Dimensión inválida. Debe estar entre [5, {dim_max}] y debe ser impar")
            except ValueError:
                print("Error: El valor ingresado debe ser un entero", file=stderr)
            except:
                print("Ha ocurrido un error inesperado")
        
        # Capturar el símbolo.
        while True:
            simb = input("Simbolo: ")
            if len(simb) == 1:
                break
            
            print("El símbolo debe contener exactamente un carácter")
        
        # Capturar si la figura sera hueca o no.
        while True:
            respuesta = input("¿Deseas qué la figura esté hueca? (y/n): ").lower()
            if respuesta == "y":
                es_hueco = True
                break
            elif respuesta == "n":
                es_hueco = False
                break
            
            print("Respuesta inválida, intente de nuevo")
            
        # Imprimir figuras segun la opción elegida.
        match opc:
            case 1:
                print(crear_reloj(dimension, simb, es_hueco))
            case 2:
                print(crear_rombo(dimension, simb, es_hueco))
            case 3:
                print(crear_monio(dimension, simb, es_hueco))
            case 4:
                print(crear_copa(dimension, simb, es_hueco))
            case 5:
                print(crear_reloj(dimension, simb, es_hueco))
                print(crear_rombo(dimension, simb, es_hueco))
                print(crear_monio(dimension, simb, es_hueco))
                print(crear_copa(dimension, simb, es_hueco))