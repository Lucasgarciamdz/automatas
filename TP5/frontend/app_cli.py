import typer
import inquirer
from yaspin import yaspin
from backend.csv_tool import create_pandas, apply_regex, DATE_RE
from tabulate import tabulate


def menu(csv_path: str = typer.Option(..., prompt="Ingrese la ruta del archivo csv")):
    csv_read_spinner = yaspin(text="Leyendo csv", color="yellow")
    apply_regex_spinner = yaspin(text="Aplicando expresiones regulares", color="yellow")

    csv_read_spinner.start()
    data = create_pandas(csv_path)
    csv_read_spinner.stop()

    apply_regex_spinner.start()
    data = apply_regex(data)
    apply_regex_spinner.stop()

    ap_list = data["MAC_AP"].unique().tolist()

    ap = inquirer.prompt([inquirer.List('ACCESS POINT', message="Seleccione un AP", choices=ap_list)])

    fechas = inquirer.prompt([
        inquirer.Text("FECHA DE INICIO", message="Ingrese la fecha de inicio (YYYY/MM/DD)", validate=lambda _, x: DATE_RE.fullmatch(x) is not None),
        inquirer.Text("FECHA DE FIN", message="Ingrese la fecha de fin (YYYY/MM/DD)", validate=lambda _, x: DATE_RE.fullmatch(x) is not None),
    ])

    fecha_i, fecha_f = fechas["FECHA DE INICIO"], fechas["FECHA DE FIN"]

    filtro = (data["MAC_AP"] == ap["ACCESS POINT"]) & (data["Inicio_de_Conexión_Dia"] >= fecha_i) & (data["Inicio_de_Conexión_Dia"] <= fecha_f)

    data = data[filtro].groupby(["Usuario"]).count().reset_index()
    users = data["Usuario"].unique()

    print("")
    print(tabulate([[user] for user in users], headers=[f"Usuarios conectados al AP {ap['ACCESS POINT']} entre {fecha_i} y {fecha_f}"], tablefmt='grid', stralign='center'))

    with open("output.csv", "w") as f:
        f.write(data.to_csv(index=False))


if __name__ == '__main__':
    typer.run(menu)