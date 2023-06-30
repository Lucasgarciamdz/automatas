
def ejercicio3(string):

    tabla = [[2, 1, 1, "", "", ""],
             [2, "", "", "", "", ""],
             [2, "", "", 3, 5, 8],
             [4, "", "", "", "", ""],
             [4, "", "", "", 5, 8],
             [7, 6, 6, "", "", ""],
             [7, "", "", "", "", ""],
             [7, "", "", "", "", 8]]

    estado = 0
    digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    for caracter in string:

        if caracter == "+" and (estado == 0 or estado == 5):
            estado = tabla[estado][1]
            continue

        if caracter == "-" and (estado == 0 or estado == 5):
            estado = tabla[estado][2]
            continue

        if caracter in digitos:
            estado = tabla[estado][0]
            continue

        if caracter == "." and estado == 2:
            estado = tabla[estado][3]
            continue

        if caracter == "e" and (estado == 2 or estado == 4):
            estado = tabla[estado][4]
            continue

        return "La cadena es invalida"

    if (estado == 2 or estado == 4 or estado == 7):
        estado = tabla[estado][5]

    if estado == 8:
        return f"La cadena es valida: {cadena}"

    else:
        return "La cadena es invalida"


if __name__ == '__main__':
    print(ejercicio3())
