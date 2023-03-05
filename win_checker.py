def comprobar_ganador(board):
    
    for fila in matriz:
        if all(elem == fila[0] for elem in fila):
            return fila[0]

   
    for j in range(len(matriz[0])):
        columna = [matriz[i][j] for i in range(len(matriz))]
        if all(elem == columna[0] for elem in columna):
            return columna[0]

    
    diagonal1 = [matriz[i][i] for i in range(len(matriz))]
    diagonal2 = [matriz[i][len(matriz)-1-i] for i in range(len(matriz))]
    if all(elem == diagonal1[0] for elem in diagonal1):
        return diagonal1[0]
    elif all(elem == diagonal2[0] for elem in diagonal2):
        return diagonal2[0]

   
    return None


