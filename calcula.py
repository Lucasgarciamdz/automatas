# Analizador sintactico predictivo para operaciones aritméticas + - % y ()

# Gramatica

# E-> E + E | E - E| E % E |(E)|i

# E → T E'
# E' → + T E' | - T E' | ε
# T → F T'
# T' → % F T' | ε
# F → ( E ) | i


def obtener_col(simbolo_entrada):
    # Returns the column index for the given input symbol
    if simbolo_entrada == "i":
        return 0
    elif simbolo_entrada == "+":
        return 1
    elif simbolo_entrada == "-":
        return 2
    elif simbolo_entrada == "%":
        return 3
    elif simbolo_entrada == "(":
        return 4
    elif simbolo_entrada == ")":
        return 5
    elif simbolo_entrada == "$":
        return 6
    else:
        return 7


def obtener_fila(no_terminal):
    # Returns the row index for the given non-terminal
    if no_terminal == "E":
        return 0
    elif no_terminal == "E'":
        return 1
    elif no_terminal == "T":
        return 2
    elif no_terminal == "T'":
        return 3
    elif no_terminal == "F":
        return 4
    else:
        return 5


class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):  # verificar si la pila está vacía
        return self.items == []

    def insertar(self, item):  # inserta elemento en la pila (cima)
        self.items.append(item)

    def extraer(self):  # extrae elemento de la pila (cima)
        return self.items.pop()

    def inspeccionar(self):  # devuelve el elemento de la cima de la pila
        return self.items[-1]

    def tamano(self):  # devuelve el tamaño de la pila
        return len(self.items)

    def contenido(self):  # devuelve el tamaño de la pila
        return self.items


tabla = [
    ["E->TE'", "", "", "", "E->TE'", "", ""],
    ["", "E'->+TE'", "E'->-TE'", "", "", "E'->e", "E'->e"],
    ["T->FT'", "", "", "", "T->FT'", "", ""],
    ["", "T'->e", "T'->e", "T'->%FT'", "", "T'->e", "T'->e"],
    ["F->i", "", "", "", "F->(E)", "", ""],
]


def check(entrada):
    pil = Pila()
    pil.insertar("$")
    pil.insertar("E")
    for item in entrada:
        try:
            position = entrada.index(item)
            item = float(item)
            entrada[position] = "i"
        except ValueError:
            continue
    entrada.append("$")
    for simbolo_entrada in entrada:
        cima_pila = pil.inspeccionar()
        while cima_pila != simbolo_entrada:
            col = obtener_col(simbolo_entrada)
            fil = obtener_fila(cima_pila)
            salida = tabla[fil][col]

            if salida != "":
                pil.extraer()
                posicion = salida.find(">")
                produccion = salida[posicion + 1 : len(salida)]
                produccion_pila = []

                for simbolo in produccion:
                    if simbolo != "'":
                        posicion_2 = produccion.find(simbolo)
                        if produccion[posicion_2 + 1 : posicion_2 + 2] == "'":
                            produccion_pila.append(simbolo + "'")
                        else:
                            produccion_pila.append(simbolo)
                for simbolo in reversed(produccion_pila):
                    if simbolo != "e":
                        pil.insertar(simbolo)

            cima_pila = pil.inspeccionar()

        if simbolo_entrada == "$" and pil.inspeccionar() == "$":
            return True
        else:
            pil.extraer()
    return False


def calculate_and_check(expression="3 + 3 + ( 5 % 2 ) - 3"):
    if check(expression.split()):
        print(f"La expresión es correcta, {eval(expression)}")
        return True
    print(f"La expresión no es correcta")
    return False


if __name__ == "__main__":
    calculate_and_check()

