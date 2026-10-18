def invertir_bwt(ultima_columna):
    """
    Invierte la transformación Burrows-Wheeler.
    
    Args:
        ultima_columna: String con la última columna de la matriz BWT
        
    Returns:
        String con la cadena original
    """
    n = len(ultima_columna)
    
    # Inicializamos con cadenas vacías
    tabla = [""] * n
    
    # Realizamos n iteraciones
    for iteracion in range(n):
        # Agregamos la última columna al inicio de cada cadena
        for i in range(n):
            tabla[i] = ultima_columna[i] + tabla[i]
        
        # Ordenamos alfabéticamente
        tabla.sort()
        
        # Opcional: mostrar el progreso
        print(f"\nRotación {iteracion + 1}:")
        for fila in tabla:
            print(fila)
    
    # La cadena original es la que comienza con $
    for fila in tabla:
        if fila[0] == '$':
            return fila

def invertir_bwt_simple(ultima_columna):
    """
    Versión simplificada sin mostrar pasos intermedios.
    """
    n = len(ultima_columna)
    tabla = [""] * n
    
    for _ in range(n):
        for i in range(n):
            tabla[i] = ultima_columna[i] + tabla[i]
        tabla.sort()
    
    # Retornar la fila que empieza con $
    for fila in tabla:
        if fila[0] == '$':
            return fila
    
    return None

def main():
    print("=" * 50)
    print("INVERSA DE LA TRANSFORMACIÓN BURROWS-WHEELER (BWT)")
    print("=" * 50)
    
    # Pedir la última columna al usuario
    print("\nIngresa la última columna de BWT:")
    print("(Usa $ como carácter terminador)")
    ultima_columna = input("Última columna: ").strip()
    
    # Validar que contenga el símbolo $
    if '$' not in ultima_columna:
        print("\n⚠️  Advertencia: La cadena debe contener el carácter '$'")
        print("Agregando '$' automáticamente...")
        ultima_columna = '$' + ultima_columna
    
    print("\n" + "=" * 50)
    print("PROCESANDO...")
    print("=" * 50)
    
    # Invertir BWT (con pasos)
    cadena_original = invertir_bwt(ultima_columna)
    
    # Mostrar resultado
    print("\n" + "=" * 50)
    print("RESULTADO")
    print("=" * 50)
    print(f"Última columna (entrada): {ultima_columna}")
    print(f"Cadena original:          {cadena_original}")
    print(f"Sin terminador:           {cadena_original.replace('$', '')}")
    print("=" * 50)

# Ejemplo de uso alternativo sin interacción
def ejemplo():
    """
    Función de ejemplo con la cadena de tu documento
    """
    print("\n" + "=" * 50)
    print("EJEMPLO CON TU CADENA")
    print("=" * 50)
    
    # Tu ejemplo
    ultima_columna = "$BCCLMOOOOOR T"
    print(f"Última columna: {ultima_columna}")
    
    resultado = invertir_bwt_simple(ultima_columna)
    print(f"\nCadena original: {resultado}")
    print(f"Sin terminador: {resultado.replace('$', '')}")

if __name__ == "__main__":
    # Descomentar la línea que quieras usar:
    
    # Opción 1: Modo interactivo (pedir entrada por teclado)
    main()
    
    # Opción 2: Ejecutar el ejemplo directamente
    # ejemplo()