def convertir_a_notacion_polaca_inversa(expresion):
    """
    Esta función convierte una expresión "normal" a notación polaca inversa

    Algoritmo:
        Entrada: Una cadena que contiene una expresión de paréntesis.
        Salida: Una cadena que contiene una expresión en notación polaca inversa.
        Mientras haya símbolos por leer:
            Lea el símbolo.
            Si es un número, entonces agréguelo a la cadena final.
            En otro caso, si es un operador:
                Mientras haya un operador de mayor jerarquía en la parte superior de la pila:
                    Retire el operador de mayor jerarquía de la pila para agregarlo a la cadena final.
                Apile el operador en la pila.
        En otro caso, si es paréntesis izquierdo, entonces apile el paréntesis a la pila.
        En otro caso, si es paréntesis derecho:
            Mientras no haya un paréntesis izquierdo en la parte superior de la pila:
                Retire los operadores de la pila para agregarlos a la cadena final.
            Retire el paréntesis izquierdo de la pila.
        Mientras haya operadores en la pila, agréguelos a la cadena final.
    """
    simbolos = expresion.split() # Entrada, delimitada por espacio
    pila = []
    expresion_final = [] # expresión final
    pasos = []  # Los pasos que se sigue para el informe

    for simbolo in simbolos:
        # Si es un número, entonces agréguelo a la cadena final.
        if simbolo.isdigit():
            expresion_final.append(simbolo)
            pasos.append(
                f"Número {simbolo} agregado al final."
            )
        # Pero si es un operador, entonces
        elif simbolo in ["+", "-", "*", "/", "**"]:
            while len(pila) > 0 and pila[-1] != "(" and jerarquia_de_operador(pila[-1]) >= jerarquia_de_operador(simbolo):
                operador = pila.pop() # Elimina el ultimo elemento de la lista y mantiene los demás
                expresion_final.append(operador)
                pasos.append(
                    operador + " retirado de la pila y agregado a la cadena final."
                )
            pila.append(simbolo) # Agrega el operador actual a la pila
            pasos.append(
                f"Operador {simbolo} agregado."
            )

        # En otro caso, si es paréntesis izquierdo, entonces apile el paréntesis a la pila.
        elif simbolo == "(":
            pila.append(simbolo)

        # En otro caso, si es paréntesis derecho:
        elif simbolo == ")":
            # Mientras no haya un paréntesis izquierdo en la parte superior de la pila
            while pila and pila[-1] != "(":
                operador = pila.pop()
                expresion_final.append(operador)  # Agrega el operador a la salida
                pasos.append(
                    f"Operador {operador} retirado de la pila y agregado a la salida."
                )
            # Retira el paréntesis izquierdo de la pila, si existe
            if pila and pila[-1] == "(":
                pila.pop()
                pasos.append(
                    f"Paréntesis izquierdo '(' encontrado y retirado."
                )

    # Mientras haya operadores en la pila, agréguelos a la cadena final.
    while pila:
        operador = pila.pop()
        expresion_final.append(operador)
        pasos.append(
            f"Operador {operador} retirado de la pila y agregado a la salida."
        )

    # Regresar los pasos y la expresión polaca inversa como string
    return " ".join(expresion_final), pasos

def jerarquia_de_operador(operador):
    """
    Esta función determina la jerarquía de los operadores **, *, /, +, -
    """
    if operador == "**":
        return 3  # Se asigna la mayor jerarquía
    elif operador in ['*', '/']:
        return 2  
    elif operador in['+', '-']:
        return 1  # Tienen la menor jerarquía
    return 0

def guardar_informe(expresion_original, resultado, pasos):
    """
    Esta función guarda un informe de la conversión hecha
    """
    reporte = open("reporte_de_conversion.txt", "w")
    reporte.write(
        "Conversión de notación 'normal' a notación polaca inversa\n"
    )
    reporte.write(
        "Expresión original: " + expresion_original + "\n"
    )
    reporte.write(
        "Expresión polaca inversa: " + resultado + "\n\n"
    )
    reporte.write(
        "Pasos de la conversión:\n"
    )
    for indice in range(len(pasos)): # Itera y agrega los pasos al reporte
        reporte.write(pasos[indice] + "\n")
    reporte.close()

def ejecutar_programa():
    """
    Función principal que ejecuta el programa
    """
    print("\nConversor de notación 'normal' a notación polaca inversa")
    # Solicitar una expresión aritmética
    expresion = input(
        """
    Escribe una expresión aritmética. (SEPARA CADA PARTE CON ESPACIOS)
    Ejemplo: 12 * ( 312 * 23 ) ** 4.
    => """
    )

    # Llama a el conversor de notacion
    resultado, pasos = convertir_a_notacion_polaca_inversa(expresion)
    
    # Verificar si la conversión fue exitosa
    if resultado and pasos:
        print(
            "Tu expresión en notación polaca inversa es:", resultado
        )
          
        # Guardar el informe en un archivo
        guardar_informe(expresion, resultado, pasos)
        print(
            "Se ha guardado un informe detallado como reporte_de_conversion.txt"
        )
    else:
        print(
            "Por favor, verifica tu expresión."
        )


if __name__ == "__main__":
    ejecutar_programa()