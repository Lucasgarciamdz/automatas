""" Analizador sintactico predictivo para operaciones aritméticas + - % y ()

Gramatica

E-> E + E | E - E| E % E |(E)|i

E → T E'
E' → + T E' | - T E' | ε
T → F T'
T' → % F T' | ε
F → ( E ) | i
"""
import pandas as pd
import time

def obtener_col(simbolo_entrada):
    columns = {"i": 0, "+": 1, "-": 2, "%": 3, "(": 4, ")": 5, "$": 6}
    return columns.get(simbolo_entrada, 7)


def obtener_fila(no_terminal):
    rows = {"E": 0, "E'": 1, "T": 2, "T'": 3, "F": 4}
    return rows.get(no_terminal, 5)


class Pila:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def insertar(self, item):
        self.items.append(item)

    def extraer(self):
        return self.items.pop()

    def inspeccionar(self):
        return self.items[-1]

    def tamano(self):
        return len(self.items)

    def contenido(self):
        return self.items


tabla = [
    ["E->TE'", "", "", "", "E->TE'", "", ""],
    ["", "E'->+TE'", "E'->-TE'", "", "", "E'->e", "E'->e"],
    ["T->FT'", "", "", "", "T->FT'", "", ""],
    ["", "T'->e", "T'->e", "T'->%FT'", "", "T'->e", "T'->e"],
    ["F->i", "", "", "", "F->(E)", "", ""],
]


# def dibujar_arbol(pila_arbol, nivel=0, pila_arbol_original=None, last=True):
#     if not pila_arbol.estaVacia():
#         node = pila_arbol.inspeccionar()
#         pila_arbol.extraer()

#         branch = "└── " if last else "├── "
#         print("".join([" " if i % 2 == 0 else "|" for i in range(nivel - 2)]) + branch + node)

#         dibujar_arbol(pila_arbol, nivel + 2, pila_arbol_original, last=True)
#         dibujar_arbol(pila_arbol, nivel + 2, pila_arbol_original, last=False)

#     return pila_arbol_original


def check(entrada):
    tabla_datos = []
    df = pd.DataFrame(columns=["Pila", "Entrada", "Salida"])

    entrada = entrada.split(" ")
    entrada = [item for item in entrada if item != ""]

    p = Pila()
    p.insertar("$")
    p.insertar("E")

    for item in entrada:
        try:
            position = entrada.index(item)
            item = float(item)
            entrada[position] = "i"
        except ValueError:
            continue

    entrada.append("$")
    salida = ""
    count = -1

    tabla_datos.append({"Pila": str(p.contenido()), "Entrada": entrada[count:], "Salida": salida})

    for simbolo_entrada in entrada:
        count += 1
        while p.inspeccionar() != simbolo_entrada:
            col = obtener_col(simbolo_entrada)
            fil = obtener_fila(p.inspeccionar())
            try:
                salida = tabla[fil][col]
            except IndexError:
                return False

            if salida != "":
                p.extraer()
                posicion = salida.find(">")
                produccion = salida[posicion + 1: len(salida)]
                produccion_pila = [simbolo + "'" if produccion[i + 1: i + 2] == "'" else simbolo for i, simbolo in enumerate(produccion) if simbolo != "'"]

            for simbolo in reversed(produccion_pila):
                if simbolo != "e":
                    p.insertar(simbolo)

            tabla_datos.append({"Pila": str(p.contenido()), "Entrada": entrada[count:], "Salida": salida})

        if simbolo_entrada == "$" and p.inspeccionar() == "$":
            df = pd.DataFrame(tabla_datos, columns=["Pila", "Entrada", "Salida"])
            print("------------ Tabla de análisis sintáctico ------------")
            print(df)
            return True
        else:
            p.extraer()
            tabla_datos.append({"Pila": str(p.contenido()), "Entrada": entrada[count:], "Salida": salida})
    return False


def calculate_and_check(expression="3 + 3 + ( 5 % 2 ) - 3"):
    print(f"Calculando: {expression} ...")
    time.sleep(1)
    if check(expression):
        print(f"\nLa expresión es correcta, {eval(expression)}")
        return True
    print("La expresión no es correcta")
    return False


if __name__ == "__main__":
    calculate_and_check()
