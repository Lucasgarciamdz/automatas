import pandas as pd
import re

# Expresiones regulares
MAC_RE = re.compile(r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):HCDD$')
DATE_RE = re.compile(r'(20(1[5-9]|2[0-5])[-/](0[1-9]|1[0-2])[-/]([0-2][0-9]|3[0-1])$)')
USER_RE = re.compile(r'[a-zA-Z0-9-_\\/]{1,25}$')


def create_pandas(csv_path: str, columns: list = ["MAC_AP", "Inicio_de_Conexión_Dia", "FIN_de_Conexión_Dia", "Usuario"]):
    data = pd.read_csv(csv_path,
                       low_memory=False,
                       usecols=columns)

    return data


def apply_regex(data: pd.DataFrame):
    mask = (data["MAC_AP"].str.fullmatch(MAC_RE) &
            data["Inicio_de_Conexión_Dia"].str.fullmatch(DATE_RE) &
            data["FIN_de_Conexión_Dia"].str.fullmatch(DATE_RE) &
            data["Usuario"].str.fullmatch(USER_RE))
    data = data[mask]

    return data


# def get_ap_list(data: pd.DataFrame):
#     return data["MAC_AP"].unique()


# if __name__ == '__main__':
#     start = time.time()
#     data = create_pandas("/Users/mymac/Downloads/export-2019-to-now-v4/export-2019-to-now-v4.csv")
#     data = apply_regex(data)
#     print(data)
#     end = time.time()
#     print(f"Tiempo de ejecucion: {end - start} segundos")
