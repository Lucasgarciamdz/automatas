from random import randint


alfabeto = ["a", "b", "c", "d", "0", "1", "2", "3", "4"]


def obtener_cadenas(x=(randint(0, len(alfabeto))), y=(randint(0, len(alfabeto)))):
    cadena_x = alfabeto[:x]
    cadena_y = alfabeto[-y:]
    return cadena_x, cadena_y


def concat(c1, c2):
    concatenacion = c1
    for i in c2:
        concatenacion.append(i)
    return concatenacion


def potencia(c, p):
    return c*p


x, y = obtener_cadenas()

print(f"La cadena x es: {x} \n La cadena y es: {y}")
print("")
print(f"El largo de la cadena x es: {len(x)}\n El largo de la cadena y es: {len(y)}")  # noqa: E501 # type: ignore
print("")
print(f"La concatenación xy es: {concat(x, y)}")
print("")
print(f"La potencia x^0 es: {potencia(x,0)}")
print("")
print(f"La potencia x^1 es: {potencia(x,1)}")
print("")
print(f"La potencia y^2 es: {potencia(y,2)}")
print("")
print(f"La potencia y^3 es: {potencia(y,3)}")
