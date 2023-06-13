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


mac_regex = r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$'
date_regex = r'(20(1[0-9]|2[0-3])[-/](0[1-9]|1[0-2])[-/]([0-2][0-9]|3[0-1])$)'
user_regex = r'([a-z]|[A-Z])*$'  

# devuelve un DataFrame de todo el csv
data = pd.read_csv("/home/franco/Escritorio/automatas-gramatica/export-2019-to-now-v4.csv", low_memory=False)

# devuelve un DataFrame de las MACs de los APs
ap_mac_list = data["MAC_AP"].unique()
ap_mac_list_sorted = []
for ap in ap_mac_list:
    if re.fullmatch(mac_regex, ap):
        with open("aps.txt", "a+") as file:
            file.write(ap + "\n")

# for mac in ap_mac_list_sorted:
#     with open("macs.txt", "a+") as file:
#         file.write(mac + "\n")

# devuelve un DataFrame de los nombres de usuarios posibles
user_list = data["Usuario"].unique()
user_list_sorted = []
for user in user_list:
    if re.fullmatch(user_regex, user):
        with open("users.txt", "a+") as file:
            file.write(user + "\n")

# for user in user_list_sorted:
#     with open("users.txt", "a+") as file:
#         file.write(user + "\n")

# Imprime la totalidad de los APs
# print("Lista APs")
# print("--------------")
# file = open("aps.txt", "r+")
# print(file.read())
# ap = input("Ingrese un AP: ")
# date_start = input("Ingrese fecha de inicio: ")
# date_end = input("Ingrese fecha de fin: ")

ap = "14-96-E5-D1-BA-89"
date_start = "2019-02-07"
date_end = "2020-02-14"


print(f'Usuarios conectados al AP {ap} entre {date_start} y {date_end}:')
users = data.loc[data["MAC_AP"] == ap]
users = users.loc[users["Inicio_de_Conexión_Dia"] > date_start]
users = users.loc[users["FIN_de_Conexión_Dia"] < date_end]["Usuario"].unique()
print(users)