def diagonal_rectangulo(ancho,alto):
    '''(number,number)->float
    >>>diagonal_rectangulo(10,6)
    11.66 '''
    suma_cuadrados = (ancho ** 2) + (alto**2)
    diagonal = math.sqrt(suma_cuadrados)
    return diagonal
