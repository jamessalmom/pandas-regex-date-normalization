"""
Normalização de datas em formatos variados.

Combina um pré-processamento com regex (unifica separadores) com
pd.to_datetime para lidar com formatos mistos (dd/mm/yyyy, dd-mm-yyyy, dd.mm.yyyy).
"""
import re
import pandas as pd


def _padroniza_separador(valor) -> str:
    valor = str(valor).strip()
    return re.sub(r'[-.]', '/', valor)


def normalizar_datas(df: pd.DataFrame, coluna: str, dayfirst: bool = True) -> pd.DataFrame:
    """
    Cria `coluna_normalizada` (datetime) a partir de uma coluna de datas
    com formatos de separador inconsistentes.

    Exemplo:
        df = normalizar_datas(df, 'data_evento')
    """
    serie_padronizada = df[coluna].apply(_padroniza_separador)
    df[f'{coluna}_normalizada'] = pd.to_datetime(serie_padronizada, dayfirst=dayfirst, errors='coerce')
    return df


if __name__ == "__main__":
    df = pd.DataFrame({"data_evento": ["01/06/2026", "02-06-2026", "03.06.2026", "inválida"]})
    print(normalizar_datas(df, "data_evento"))
