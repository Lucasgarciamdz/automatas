# aca el programa tiene que hacer las cosas importantes por eso se llama main (:
"""

Tareas:

- Expresion regular para MACs de APs (columna: MAC_AP) y largar lista de APs
- Asignar nombre a cada AP 
- Expresion regular para fechas (Columna: Inicio_de_conexio_dia y Fin_de_conexio_dia)
- Expresion regular para usuarios (Columna: Usuario) y largar lista de usuarios
- Vamos a usar el modulo Pandas para manipular el csv
- Vamos a usar el modulo re para las expresiones regulares

13/06/2023:

- Ya estan todas las REGEX (chequear que esten bien)
- La logica y manejo del csv ya estaria (refactorizable igual)
- Hice testing para las REGEX

"""

import re
import pandas as pd


# Imprime la totalidad de los APs y pide que le pasemos uno junto con la fecha de inicio y fin de sesion
def aps():
    print("Lista APs")
    print("--------------")
    print(ap_mac_list)
    ap = input("Ingrese un AP: ")
    date_start = input("Ingrese fecha de inicio: ")
    date_end = input("Ingrese fecha de fin: ")
    return ap, date_start, date_end

# Devulve los usuarios conectados dado un cierto AP, fecha de inicio de sesion y fecha de fin de sesion
def obtain():
    # ap, date_start, date_end = aps()
    ap = "04-18-D6-22-38-E1:HCDD"
    date_start = "2019-02-07"
    date_end = "2020-02-14"
    print(f'Usuarios conectados al AP {ap} entre {date_start} y {date_end}:')
    users = data.loc[data["MAC_AP"] == ap ]
    users = users.loc[users["Inicio_de_Conexión_Dia"] > date_start]
    users = users.loc[users["FIN_de_Conexión_Dia"] < date_end]["Usuario"].unique()
    print(users)

if __name__ == '__main__':

    # definimos las expresiones regulares
    mac_regex = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):HCDD$')
    date_regex = re.compile(r'(20(1[0-9]|2[0-3])[-/](0[1-9]|1[0-2])[-/]([0-2][0-9]|3[0-1])$)')
    user_regex = re.compile(r'([a-z]|[A-Z])*$')

    # devuelve un DataFrame de las columnas que vamos a ocupar del csv
    data = pd.read_csv("/home/franco/Escritorio/automatas-gramatica/export-2019-to-now-v4.csv", 
                    low_memory=False, 
                    usecols=["MAC_AP", "Inicio_de_Conexión_Dia", "FIN_de_Conexión_Dia", "Usuario"])

    # filtra los datos que no cumplen con las expresiones regulares
    data = data[data["MAC_AP"].apply(lambda x: mac_regex.fullmatch(str(x)) is not None) &
                        data["Inicio_de_Conexión_Dia"].apply(lambda x: date_regex.fullmatch(str(x)) is not None) &
                        data["FIN_de_Conexión_Dia"].apply(lambda x: date_regex.fullmatch(str(x)) is not None) &
                        data["Usuario"].apply(lambda x: user_regex.fullmatch(str(x)) is not None)]


    # devuelve un DataFrame de las MACs de los APs
    ap_mac_list = data["MAC_AP"].unique()

    # devuelve un DataFrame de los nombres de usuarios posibles
    user_list = data["Usuario"].unique()

    obtain()

