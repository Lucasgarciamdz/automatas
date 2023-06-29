import pandas as pd
import unittest
from csv_tool import apply_regex, MAC_RE, DATE_RE, USER_RE
import pdb
from parameterized import parameterized


class TestCsvTool(unittest.TestCase):
    def test_apply_regex(self):
        # Create test data
        INICIO_DE_CONEXION_DIA = "Inicio_de_Conexión_Dia"
        FIN_DE_CONEXION_DIA = "FIN_de_Conexión_Dia"

        data = pd.DataFrame({
            "MAC_AP": ["00:11:22:33:44:55:HCDD", "001122334455:HCDD", "00:11:22:33:44:52:HCDD"],
            INICIO_DE_CONEXION_DIA: ["2022-01-01", "1900-01-01", "2022-01-02"],
            FIN_DE_CONEXION_DIA: ["2022-01-02", "1800-01-01", "2022-01-03"],
            "Usuario": ["invitado-lucas1", "@ hola_ 3242", "invitado-franco2"]
        })

        # Apply regex
        result = apply_regex(data)
        # Check that only valid rows are returned
        self.assertEqual(len(result), 2)
        self.assertEqual(result.iloc[0]["MAC_AP"], "00:11:22:33:44:55:HCDD")
        self.assertEqual(result.iloc[0][INICIO_DE_CONEXION_DIA], "2022-01-01")
        self.assertEqual(result.iloc[0][FIN_DE_CONEXION_DIA], "2022-01-02")
        self.assertEqual(result.iloc[0]["Usuario"], "invitado-lucas1")
        self.assertEqual(result.iloc[1]["MAC_AP"], "00:11:22:33:44:52:HCDD")
        self.assertEqual(result.iloc[1][INICIO_DE_CONEXION_DIA], "2022-01-02")
        self.assertEqual(result.iloc[1][FIN_DE_CONEXION_DIA], "2022-01-03")
        self.assertEqual(result.iloc[1]["Usuario"], "invitado-franco2")

    @parameterized.expand([1, 2, 3])
    def test_regex(self):
        

if __name__ == '__main__':
    unittest.main()
