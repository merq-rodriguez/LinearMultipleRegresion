
def GaussJordan(matrix):
    for i in range(min(len(matrix), len(matrix[0]))):
        for r in range(i, len(matrix)):
            ceros_fila = matrix[r][i] == 0
            if ceros_fila:
                continue
            matrix[i], matrix[r] = matrix[r], matrix[i]
            Ifila_columna = matrix[i][i]
            for w in range(i + 1, len(matrix)):
                IFila = matrix[w][i]
                escalarM =  IFila / Ifila_columna * -1 
                for a in range(i, len(matrix[0])):
                    matrix[w][a] += matrix[i][a] * escalarM
            break
    
    for i in range(min(len(matrix), len(matrix[0])) - 1, -1, -1):
        Ielemento_columna = -1
        Ielemento = -1
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                continue
            if Ielemento_columna == -1:
                Ielemento_columna = j
                Ielemento = matrix[i][j]
            matrix[i][j] /= Ielemento

        for k in range(i):
            fila_encima = matrix[k][Ielemento_columna]
            escalarM = -1 * fila_encima
            for a in range(len(matrix[0])):
                matrix[k][a] += matrix[i][a] * escalarM

    return matrix
    



