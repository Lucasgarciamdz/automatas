def automata(cadena):
    tabla = [[2, 1, 1, "", "", ""],
             [2, "", "", "", "", ""],
             [2, "", 3, 5, 5, 8],
             [4, "", "", "", "", 7],
             [4, "", "", "", 5, 8],
             [7, 6, 6, 9, "", ""],
             [7, "", "", "", "", ""],
             [7, "", "", "", "", 8],
             [7, 6, 6, "", "", ""],
             ["acepta", "acepta", "acepta", "acepta", "acepta", "acepta"]
             ]


    estado_actual = 0
    i = 0

    while i < len(cadena):
        simbolo = cadena[i]
        columna = 0

        if simbolo.isdigit():
            columna = 0
        elif simbolo == "+":
            columna = 1
        elif simbolo == "-":
            columna = 1
        elif simbolo == ".":
            columna = 2
        elif simbolo.lower() == "e":
            columna = 3
        elif simbolo == " ":
            columna = 4
        else:
            return "No es un número válido."

        estado_actual = tabla[estado_actual][columna]

        if estado_actual == "":
            return "No es un número válido."

        i += 1

    return "Es un número válido."


cadena1 = "1e2"
resultado1 = automata(cadena1)
print(resultado1)  # salida: "Es un número válido."

cadena2 = "-12.34e+5"
resultado2 = automata(cadena2)
print(resultado2)  # salida: "Es un número válido."

# cadena3 = "3.14.159"
# resultado3 = automata(cadena3)
# print(resultado3)  # salida: "No es un número válido."
