# Normalização de datas (Junho)

Método pandas + regex que combina um pré-processamento (unifica
separadores) com `pd.to_datetime` para lidar com formatos mistos
(dd/mm/yyyy, dd-mm-yyyy, dd.mm.yyyy).

## Uso
```python
import pandas as pd
from normalizar_datas import normalizar_datas

df = pd.DataFrame({"data_evento": ["01/06/2026", "02-06-2026", "03.06.2026"]})
df = normalizar_datas(df, "data_evento")
```
