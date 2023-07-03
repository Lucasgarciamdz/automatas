import typer
import inquirer
from yaspin import yaspin
from csv_tool import DATE_RE, apply_regex, create_pandas
from tabulate import tabulate
import pandas as pd


def menu(csv_path: str = typer.Option(..., prompt="Ingrese la ruta del archivo csv")):

    INICIO_CONEXION_DIA = "Inicio_de_Conexión_Dia"
    FIN_CONEXION_DIA = "FIN_de_Conexión_Dia"

    with yaspin(text="Leyendo csv", color="yellow"):
        data = create_pandas(csv_path)

    with yaspin(text="Aplicando expresiones regulares", color="yellow"):
        data = apply_regex(data)

    ap_list = data["MAC_AP"].unique().tolist()

    while True:
        ap = inquirer.prompt(
            [inquirer.List("ACCESS POINT", message="Seleccione un AP", choices=ap_list)]
        )

        fechas = inquirer.prompt(
            [
                inquirer.Text(
                    "FECHA DE INICIO",
                    message="Ingrese la fecha de inicio (YYYY-MM-DD)",
                    validate=lambda _, x: DATE_RE.fullmatch(x) is not None,
                ),
                inquirer.Text(
                    "FECHA DE FIN",
                    message="Ingrese la fecha de fin (YYYY-MM-DD)",
                    validate=lambda _, x: DATE_RE.fullmatch(x) is not None,
                ),
            ]
        )

        ap, fecha_i, fecha_f = (
            ap["ACCESS POINT"],
            pd.to_datetime(fechas["FECHA DE INICIO"]),
            pd.to_datetime(fechas["FECHA DE FIN"]),
        )

        data[INICIO_CONEXION_DIA] = pd.to_datetime(data[INICIO_CONEXION_DIA])
        data[FIN_CONEXION_DIA] = pd.to_datetime(data[FIN_CONEXION_DIA])

        filtro = (
            (data["MAC_AP"] == ap) &
            (
                (data[INICIO_CONEXION_DIA].between(fecha_i, fecha_f)) |
                (data[FIN_CONEXION_DIA].between(fecha_i, fecha_f)) |
                (data[INICIO_CONEXION_DIA] <= fecha_i) & (data[FIN_CONEXION_DIA] >= fecha_f)
            )
        )

        data = data.loc[filtro]
        users = data["Usuario"].unique()

        consulta = f'Usuarios conectados al AP {ap} entre {fecha_i} y {fecha_f}'
        print("")
        print(
            tabulate(
                [[user] for user in users],
                headers=[
                    consulta
                ],
                tablefmt="grid",
                stralign="center",
            )
        )

        if typer.confirm("¿Desea guardar los datos en un archivo csv?"):
            write_to_csv(data, consulta)

        if not typer.confirm("¿Desea realizar otra consulta?"):
            print("Gracias por usar nuestro programa")
            break


def write_to_csv(data: pd.DataFrame, consulta: str):
    file_name = f'output_{consulta}.csv'
    data.to_csv(file_name, index=False)


if __name__ == "__main__":
    typer.run(menu)
