import pandas as pd
import typer
import inquirer
from yaspin import yaspin
from csv_tool import create_pandas, apply_regex, get_ap_list, DATE_RE, MAC_RE, USER_RE
from tabulate import tabulate


def menu(csv_path: str = typer.Option(..., prompt="Ingrese la ruta del archivo csv")):
    csv_read_spinner = yaspin(text="Leyendo csv", color="yellow")
    apply_regex_spinner = yaspin(text="Aplicando expresiones regulares", color="yellow")

    csv_read_spinner.start()
    data = create_pandas(csv_path, columns_list)
    csv_read_spinner.stop()

    apply_regex_spinner.start()
    data = apply_regex(data)
    apply_regex_spinner.stop()

    ap_list = data["MAC_AP"].unique().tolist()
    ap_spinner = yaspin(text="Cargando lista de APs", color="yellow")
    ap_spinner.start()
    ap = inquirer.prompt([inquirer.List('ACCESS POINT', message="Seleccione un AP", choices=ap_list)])
    ap_spinner.stop()

    fechas = inquirer.prompt([
        inquirer.Text("FECHA DE INICIO", message="Ingrese la fecha de inicio", validate=lambda _, x: DATE_RE.fullmatch(x) is not None),
        inquirer.Text("FECHA DE FIN", message="Ingrese la fecha de fin", validate=lambda _, x: DATE_RE.fullmatch(x) is not None),
    ])
    fecha_i, fecha_f = fechas["FECHA DE INICIO"], fechas["FECHA DE FIN"]

    mask = (data["MAC_AP"] == ap["ACCESS POINT"]) & (data["Inicio_de_Conexión_Dia"] >= fecha_i) & (data["Inicio_de_Conexión_Dia"] <= fecha_f)
    users = data[mask]["Usuario"].unique()

    users_spinner = yaspin(text="Cargando usuarios", color="yellow")
    users_spinner.start()
    print(tabulate([[user] for user in users], headers=[f"Usuarios conectados al AP {ap['ACCESS POINT']} entre {fecha_i} y {fecha_f}"]))
    users_spinner.stop()


if __name__ == '__main__':
    typer.run(menu)
