import pandas as pd
import re

# Expresiones regulares
MAC_RE = re.compile(r"([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2}):HCDD$")
DATE_RE = re.compile(r"(20(1[5-9]|2[0-5])[-/](0[1-9]|1[0-2])[-/]([0-2]\d|3[0-1])$)")
USER_RE = re.compile(r"[a-zA-Z0-9-_\\/]{1,25}$")


def create_pandas(csv_path: str, columns: list = ["MAC_AP", "Inicio_de_Conexión_Dia", "FIN_de_Conexión_Dia", "Usuario"]) -> pd.DataFrame:

    data = pd.read_csv(csv_path, low_memory=False, usecols=columns)

    return data


def apply_regex(data: pd.DataFrame) -> pd.DataFrame:
    filtro = (
        data["MAC_AP"].apply(lambda x: bool(re.fullmatch(MAC_RE, str(x))))
        & data["Inicio_de_Conexión_Dia"].apply(lambda x: bool(re.fullmatch(DATE_RE, str(x))))
        & data["FIN_de_Conexión_Dia"].apply(lambda x: bool(re.fullmatch(DATE_RE, str(x))))
        & data["Usuario"].apply(lambda x: bool(re.fullmatch(USER_RE, str(x))))
    )
    data = data[filtro]

    return data
