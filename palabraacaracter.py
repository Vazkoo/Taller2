
def chain_byte(value):

    # Lista para almacenar los valores binarios
    binarios = []
    
    # Recorrer cada carácter en la cadena
    for caracter in value:
        # Obtener el valor ASCII del carácter
        valor_ascii = ord(caracter)
        
        # Convertir el valor ASCII a binario y eliminar el prefijo '0b'
        binario = bin(valor_ascii)[2:]
        
        # Para asegurarnos de que tenga 8 bits, rellenamos con ceros a la izquierda
        binario = binario.zfill(8)
        
        # Añadir el valor binario a la lista
        binarios.append(binario)
    
    # Unir todos los valores binarios con un espacio
    return binarios
