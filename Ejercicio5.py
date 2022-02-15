#Enunciado: Convierte un Excel a CSV
#Objetivo:
# Aprender a trabajar con ficheros
# Usar la librería pandas de Python

import pandas as pd
read_file = pd.read_excel("HistoricoEuromillones.xlsx")
print(read_file)

read_file.to_csv("HistoricoEuromillones.csv",
                 index = None,
                 header=True)

df = pd.DataFrame(pd.read_csv("HistoricoEuromillones.csv"))

